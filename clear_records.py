"""
Script to clear all sessions, attendance, attendanceByDate, and session_photos from Firebase.
Run once to wipe old records so new punch-in/out photos appear cleanly.
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

nodes_to_clear = ['sessions', 'attendance', 'attendanceByDate', 'session_photos']

for node in nodes_to_clear:
    ref = db.reference(node)
    data = ref.get()
    count = len(data) if isinstance(data, dict) else 0
    ref.delete()
    print(f"✅ Cleared '{node}' — {count} record(s) removed")

print("\nDone. All old session and attendance records have been deleted.")
print("New records created from the app will now appear with punch-in/out photos.")
