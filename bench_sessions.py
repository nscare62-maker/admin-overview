import time
from app import app

print('imported app', flush=True)
client = app.test_client()
print('client ready', flush=True)
with client.session_transaction() as sess:
    sess['logged_in'] = True
    sess['username'] = 'admin'
print('session set', flush=True)

start = time.time()
print('before /sessions', flush=True)
resp = client.get('/sessions')
print('after /sessions', resp.status_code, round(time.time() - start, 6), flush=True)

start = time.time()
print('before session detail', flush=True)
resp2 = client.get('/sessions/-OwVtfDk4-F2OwEK40bn')
print('after session detail', resp2.status_code, round(time.time() - start, 6), flush=True)
print(resp2.get_data(as_text=True)[:300], flush=True)
