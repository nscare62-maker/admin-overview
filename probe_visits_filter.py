from app import app, read_firebase_path

client = app.test_client()
with client.session_transaction() as sess:
    sess['logged_in'] = True
    sess['username'] = 'admin'

for query in [
    '/visits',
    '/visits?employee=8925533755',
    '/visits?employee=EMP9492',
    '/visits?employee=Girija',
    '/visits?date=2026-04-19',
    '/visits?employee=8925533755&date=2026-04-19',
]:
    resp = client.get(query)
    body = resp.get_data(as_text=True)
    print('QUERY', query, 'STATUS', resp.status_code)
    print('no visits?', 'No visits found for the selected filters' in body)
    print('contains total badge', 'Total: ' in body)
    print('first 250 chars:', body[:250])
    print('---')
