from app import app

client = app.test_client()
with client.session_transaction() as sess:
    sess['logged_in'] = True
    sess['username'] = 'admin'

resp = client.get('/sessions/-OwVtfDk4-F2OwEK40bn', follow_redirects=True)
print('status', resp.status_code)
print(resp.get_data(as_text=True)[:1500])
