"""
Audit session photo storage status.

This script checks every session in Firebase and reports:
- sessions whose start/end photo fields point to local device paths
- whether matching session_photos entries exist
- whether the app can resolve a web-displayable image for each side
"""

from app import load_session_photo
import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

load_dotenv()

try:
    firebase_admin.get_app()
except ValueError:
    cred_path = os.path.join(os.path.dirname(__file__), 'firebase-credentials.json')
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL', 'https://login-otp-29372-default-rtdb.firebaseio.com')
    })


def is_device_path(value):
    return isinstance(value, str) and value.startswith(('/data/', 'file://', 'content://'))


sessions = db.reference('sessions').get() or {}
photos = db.reference('session_photos').get() or {}

print('=== SESSION PHOTO AUDIT ===')
print(f'Total sessions: {len(sessions)}')
print(f'Total session_photos entries: {len(photos)}')
print()

local_only_count = 0
web_visible_count = 0

for session_id, session_data in sessions.items():
    start_uri = session_data.get('startPhotoUri')
    end_uri = session_data.get('endPhotoUri')

    start_local = is_device_path(start_uri)
    end_local = is_device_path(end_uri)

    if not start_local and not end_local:
        continue

    local_only_count += 1
    print(f'Session: {session_id}')
    if start_local:
        print('  startPhotoUri -> local device path (not web-displayable):', start_uri)
    if end_local:
        print('  endPhotoUri   -> local device path (not web-displayable):', end_uri)

    matching = []
    for photo_id, photo_data in photos.items():
        if str(photo_data.get('sessionId')) == str(session_id):
            matching.append((photo_id, photo_data))

    if matching:
        print('  session_photos entries found:')
        for photo_id, photo_data in matching:
            print(f'    - {photo_id}: type={photo_data.get("photoType") or photo_data.get("type")}, has_base64={bool(photo_data.get("imageBase64"))}')
    else:
        print('  session_photos entries found: none')

    start_resolved = bool(load_session_photo(session_id, 'start', session_data))
    end_resolved = bool(load_session_photo(session_id, 'end', session_data))
    print(f'  app can resolve start photo? {start_resolved}')
    print(f'  app can resolve end photo?   {end_resolved}')
    print()

print(f'\nSessions with local device photo paths: {local_only_count}')
print('These will not display in the web dashboard unless uploaded to Firebase as web-readable data.')
