import json
import os
from firebase_admin import credentials, db, initialize_app
from dotenv import load_dotenv

load_dotenv()
cred = credentials.Certificate('firebase-credentials.json')
initialize_app(cred, {'databaseURL': os.getenv('FIREBASE_DATABASE_URL')})

for path in ['users', 'visits', 'sessions']:
    data = db.reference(path).get() or {}
    print(f'--- {path} count={len(data)}')
    for idx, (k, v) in enumerate(list(data.items())[:3], start=1):
        print(f'KEY {idx}: {k}')
        print(json.dumps(v, indent=2)[:4000])
        print()
