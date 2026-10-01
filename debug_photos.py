"""
Debug script to check what photo data exists in Firebase for sessions.
"""
import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

load_dotenv()

cred_path = os.path.join(os.path.dirname(__file__), 'firebase-credentials.json')
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL', 'https://login-otp-29372-default-rtdb.firebaseio.com')
})

print("=" * 60)
print("SESSIONS:")
print("=" * 60)
sessions = db.reference('sessions').get() or {}
for sid, s in sessions.items():
    print(f"\nSession ID: {sid}")
    print(f"  startPhotoUri: {str(s.get('startPhotoUri', 'MISSING'))[:80]}")
    print(f"  endPhotoUri:   {str(s.get('endPhotoUri', 'MISSING'))[:80]}")
    print(f"  status:        {s.get('status')}")
    print(f"  employeeId:    {s.get('employeeId')}")

print("\n" + "=" * 60)
print("SESSION_PHOTOS:")
print("=" * 60)
photos = db.reference('session_photos').get() or {}
if not photos:
    print("  (empty)")
for pid, p in photos.items():
    print(f"\nPhoto ID: {pid}")
    print(f"  sessionId:  {p.get('sessionId')}")
    print(f"  photoType:  {p.get('photoType')}")
    print(f"  type:       {p.get('type')}")
    b64 = p.get('imageBase64', '')
    print(f"  imageBase64 length: {len(b64)} chars, starts with: {b64[:40]}")

print("\n" + "=" * 60)
print("ALL TOP-LEVEL FIREBASE NODES (checking for photo storage):")
print("=" * 60)
root = db.reference('/').get() or {}
for key in root.keys():
    val = root[key]
    count = len(val) if isinstance(val, dict) else '(not a dict)'
    print(f"  {key}: {count}")
