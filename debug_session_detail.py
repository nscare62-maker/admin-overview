import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db
from app import get_employee_reference, get_employee_by_id, load_session_photo, normalize_visit_datetime, get_session_locations

load_dotenv()
if not firebase_admin._apps:
    cred = credentials.Certificate(os.path.abspath('firebase-credentials.json'))
    firebase_admin.initialize_app(cred, {'databaseURL': os.getenv('FIREBASE_DATABASE_URL')})

session_id = '-OwVtfDk4-F2OwEK40bn'
session = db.reference(f'sessions/{session_id}').get()
print('session loaded', type(session).__name__, len(session) if isinstance(session, dict) else None)
emp_id = get_employee_reference(session)
print('emp_id', emp_id)
all_employees = db.reference('users').get() or {}
print('employees count', len(all_employees))
employee = get_employee_by_id(all_employees, emp_id)
print('employee', employee)
start_photo = load_session_photo(session_id, 'start', session)
print('start_photo', start_photo)
end_photo = load_session_photo(session_id, 'end', session)
print('end_photo', end_photo)

session['id'] = session_id
session['employeeId'] = emp_id or session.get('employeeId') or 'N/A'
session['employeeName'] = employee.get('name', session.get('employeeName', 'Unknown'))
session['employeePhone'] = employee.get('phone', session.get('employeePhone', 'N/A'))
session['employeeRole'] = employee.get('role', session.get('employeeRole', 'N/A'))
session['startPhoto'] = start_photo
session['endPhoto'] = end_photo

route_points = []
start_time = normalize_visit_datetime(session.get('startTime'))['sort_key']
end_time = normalize_visit_datetime(session.get('endTime'))['sort_key']
current_time = __import__('datetime').datetime.now().timestamp()
if not end_time:
    end_time = current_time

start_location = session.get('startLocation') or {}
if start_location.get('latitude') and start_location.get('longitude'):
    route_points.append({
        'latitude': start_location['latitude'],
        'longitude': start_location['longitude'],
        'label': 'Work started',
        'timestamp': session.get('startTime')
    })

locs = get_session_locations(session_id)
print('locs count', len(locs))
for location_id, location in locs.items():
    if not location.get('latitude') or not location.get('longitude'):
        continue
    point_time = normalize_visit_datetime(location.get('timestamp'))['sort_key']
    if point_time and (not start_time or point_time >= start_time) and point_time <= end_time:
        route_points.append({
            'latitude': location['latitude'],
            'longitude': location['longitude'],
            'label': 'Employee movement',
            'timestamp': location.get('timestamp'),
            'id': location_id
        })

end_location = session.get('endLocation') or {}
if end_location.get('latitude') and end_location.get('longitude'):
    route_points.append({
        'latitude': end_location['latitude'],
        'longitude': end_location['longitude'],
        'label': 'Work ended',
        'timestamp': session.get('endTime')
    })

route_points.sort(key=lambda point: normalize_visit_datetime(point.get('timestamp'))['sort_key'])
session['routePoints'] = route_points
print('route_points len', len(route_points))
print('first point', route_points[0] if route_points else None)
