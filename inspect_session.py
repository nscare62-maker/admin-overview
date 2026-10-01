import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db

load_dotenv()
if not firebase_admin._apps:
    cred = credentials.Certificate(os.path.abspath('firebase-credentials.json'))
    firebase_admin.initialize_app(cred, {'databaseURL': os.getenv('FIREBASE_DATABASE_URL')})

session = db.reference('sessions/-OwVtfDk4-F2OwEK40bn').get()
print('type', type(session).__name__)
print('keys', list(session.keys()) if isinstance(session, dict) else None)
print('startPhotoUri', session.get('startPhotoUri'))
print('endPhotoUri', session.get('endPhotoUri'))
print('raw session', session)
