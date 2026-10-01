from app import app

app.config['TESTING'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

client = app.test_client()
with client.session_transaction() as sess:
    sess['logged_in'] = True
    sess['username'] = 'admin'

resp = client.get('/sessions/-OwVtfDk4-F2OwEK40bn')
print('status', resp.status_code)
print('location', resp.headers.get('Location'))
print(resp.get_data(as_text=True)[:1500])
