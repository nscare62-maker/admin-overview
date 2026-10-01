import time
from app import read_firebase_path

start = time.time()
data = read_firebase_path('session_photos')
print('count', len(data) if isinstance(data, dict) else 'non-dict')
print('elapsed', round(time.time() - start, 6))
