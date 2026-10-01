"""
Backfill browser-readable session photos into Firebase `session_photos`.

This script helps when old sessions store local Android file paths like:
    /data/user/0/com.vtrace.attendance/cache/photo_1785979552268.jpg

The web dashboard cannot load those local paths. If you copy those files into a
folder on this machine, this script will upload them into Firebase as
`session_photos` entries with `imageBase64`, which the dashboard can display.

Usage:
    1. Copy the device photo files into a local folder, for example:
           D:\session-photo-backup\

    2. Run:
           .\.venv\Scripts\python.exe backfill_session_photos.py

    3. Set PHOTO_ROOT to that folder if needed, for example:
           $env:PHOTO_ROOT='D:\session-photo-backup'
           .\.venv\Scripts\python.exe backfill_session_photos.py
"""

from pathlib import Path
import base64
import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()

try:
    firebase_admin.get_app()
except ValueError:
    cred_path = Path(__file__).resolve().parent / 'firebase-credentials.json'
    cred = credentials.Certificate(str(cred_path))
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL', 'https://login-otp-29372-default-rtdb.firebaseio.com')
    })

ROOT = Path(os.getenv('PHOTO_ROOT', '.')).resolve()


def is_local_device_path(value):
    return isinstance(value, str) and value.startswith(('/data/', 'file://', 'content://'))


def find_photo_file(filename: str):
    if not ROOT.exists():
        return None

    for file_path in ROOT.rglob('*'):
        if file_path.is_file() and file_path.name == filename:
            return file_path
    return None


sessions = db.reference('sessions').get() or {}
existing_photos = db.reference('session_photos').get() or {}

print('=== BACKFILL SESSION PHOTOS ===')
print(f'PHOTO_ROOT={ROOT}')
print(f'Total sessions: {len(sessions)}')
print(f'Total existing session_photos entries: {len(existing_photos)}')
print()

backfilled = 0
skipped = 0
not_found = []

for session_id, session_data in sessions.items():
    for photo_type in ('start', 'end'):
        photo_uri = session_data.get(f'{photo_type}PhotoUri')
        if not is_local_device_path(photo_uri):
            continue

        filename = Path(photo_uri).name
        source_file = find_photo_file(filename)

        if not source_file:
            not_found.append((session_id, photo_type, filename))
            continue

        # Avoid duplicates if already present
        already_exists = False
        for photo_id, photo_data in existing_photos.items():
            if str(photo_data.get('sessionId')) == str(session_id) and (
                str(photo_data.get('photoType') or photo_data.get('type') or '').lower() == photo_type
            ):
                already_exists = True
                break

        if already_exists:
            skipped += 1
            continue

        image_bytes = source_file.read_bytes()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')

        payload = {
            'sessionId': str(session_id),
            'photoType': photo_type,
            'imageBase64': f'data:image/jpeg;base64,{image_base64}',
            'createdAt': int(__import__('time').time() * 1000)
        }

        # Store as a new session_photos entry
        db.reference('session_photos').push(payload)
        backfilled += 1
        print(f'Backfilled {photo_type} photo for session {session_id} from {source_file}')

print()
print(f'Backfilled entries: {backfilled}')
print(f'Skipped existing entries: {skipped}')
print(f'Not found locally: {len(not_found)}')

if not_found:
    print('\nPhotos not found in PHOTO_ROOT:')
    for session_id, photo_type, filename in not_found[:50]:
        print(f'  - session {session_id}, {photo_type}: {filename}')

    if len(not_found) > 50:
        print('  ... and more')
