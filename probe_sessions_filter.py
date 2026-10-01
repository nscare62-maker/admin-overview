from app import app

client = app.test_client()
with client.session_transaction() as sess:
    sess['logged_in'] = True
    sess['username'] = 'admin'

for query in [
    '/sessions',
    '/sessions?employee=8925533755',
    '/sessions?employee=EMP9492',
    '/sessions?employee=Girija',
    '/sessions?employee=Hemavathi+I',
]:
    resp = client.get(query)
    print('QUERY', query, 'STATUS', resp.status_code)
    body = resp.get_data(as_text=True)
    print('contains "No sessions found"', 'No sessions found for the selected filters' in body)
    print('contains "View Punch In/Out Photos"', 'View Punch In/Out Photos' in body)
    print('total badge count maybe', body.count('Total:'))
    print('first 300 chars', body[:300])
    print('---')
