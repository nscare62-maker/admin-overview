import time
from app import read_firebase_path, app

print('start read sessions', flush=True)
start = time.time()
sessions = read_firebase_path('sessions')
print('sessions loaded', len(sessions), round(time.time() - start, 6), flush=True)

print('start read users', flush=True)
start = time.time()
users = read_firebase_path('users')
print('users loaded', len(users), round(time.time() - start, 6), flush=True)

client = app.test_client()
with client.session_transaction() as sess:
    sess['logged_in'] = True
    sess['username'] = 'admin'

start = time.time()
print('before /sessions', flush=True)
resp = client.get('/sessions')
print('sessions status', resp.status_code, round(time.time() - start, 6), flush=True)

start = time.time()
print('before /sessions/<id>', flush=True)
resp2 = client.get('/sessions/-OwVtfDk4-F2OwEK40bn')
print('detail status', resp2.status_code, round(time.time() - start, 6), flush=True)
print(resp2.get_data(as_text=True)[:250], flush=True)
