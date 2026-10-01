from app import read_firebase_path, get_employee_reference

visits = read_firebase_path('visits')
users = read_firebase_path('users')
print('visits count', len(visits))
for visit_id, visit in list(visits.items())[:5]:
    print('VISIT', visit_id)
    print('keys', list(visit.keys()))
    print('employee ref', get_employee_reference(visit))
    print('raw', visit)
    print('---')

print('users count', len(users))
for user_id, user in list(users.items())[:5]:
    print('USER', user_id, user)
