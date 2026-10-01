from app import read_firebase_path, get_employee_filter_candidates, get_employee_reference, get_employee_by_id

all_visits = read_firebase_path('visits')
all_employees = read_firebase_path('users')

print('visits count', len(all_visits))
print('users count', len(all_employees))

sample_visits = list(all_visits.items())[:10]
for vid, v in sample_visits:
    emp_ref = get_employee_reference(v)
    print('VISIT', vid)
    print('  emp_ref', emp_ref)
    print('  keys', sorted(k for k in v.keys() if k.lower().startswith('employee') or k in ['phone', 'empPhone', 'sessionId', 'createdAt', 'timestamp']))
    print('  employeeData', get_employee_by_id(all_employees, emp_ref))
    print()

for value in ['8925533755', 'EMP9492', 'Girija', 'Mohan']:
    cands = get_employee_filter_candidates(all_employees, value)
    print('FILTER', value, '->', sorted(cands))
