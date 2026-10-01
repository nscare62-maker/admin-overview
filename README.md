# S2C Admin Dashboard - Employee Monitoring System

A comprehensive Flask-based web dashboard for monitoring, managing, and tracking employees, field visits, tasks, and field operations in the S2C (Start-to-Close) management system.

---

## 🎯 Features & Modules

### 📊 1. Dashboard Overview
- **Real-Time KPI Cards:** Active sessions, total employees, today's attendance count, and pending permission requests.
- **Quick Action Links:** Fast navigation to assign tasks, check attendance, or inspect field activities.
- **System Diagnostics:** Live Firebase database connection status, server health, and real-time clock.

### 👥 2. Employee Management
- **Directory & Search:** Search and filter full employee roster by department, role, or active status.
- **Add & Edit Profiles:** Create new staff profiles or modify existing contact and job details.
- **Individual Detail Pages:** Complete timeline of recent sessions, visits, and historical attendance.
- **Credential Management:** Reset employee credentials securely from the dashboard.

### 📅 3. Attendance Management
- **Attendance Records:** Real-time log of daily punch-ins and punch-outs.
- **Status Classification:** Automatic categorization for On Time, Late Start, and Half Day.
- **Approval Actions:** Review, approve, or reject late starts and half days with remarks.
- **Date Filtering:** Quick filtering by specific dates or employee IDs.

### 📝 4. Permission & Leave Management
- **Request Workflows:** Manage Late Start requests and Leave types (Casual Leave, Medical Leave, Emergency, Planned).
- **Status Filter:** Categorize requests by Pending, Approved, or Rejected.
- **Manager Remarks:** Add administrative remarks and decisions with timestamps.

### ⏰ 5. Work Session Monitoring
- **Live Session Tracking:** Monitor ongoing work sessions in real time.
- **Duration Metrics:** Automatic breakdown of total work hours versus break periods.
- **Detailed Audits:** Audit punch-in/out timestamps, GPS coordinates, and session photos.

### 📍 6. Field Visits Tracking
- **Field Staff Visits:** Track on-ground visits to clients, farmers, and partner sites.
- **Location Audits:** Geo-tagged visit locations and check-in coordinates.
- **Visit Details:** Review visit purposes, meeting outcomes, notes, and photos.

### 📋 7. Task Management (Field & Office)
- **Dual Assignment Workflows:** Dedicated assignment forms for Field Tasks and Office Tasks.
- **Priority & Deadlines:** Set priority levels (Low, Medium, High, Urgent) and due dates.
- **Status Tracking:** Track tasks through Pending, In Progress, and Completed states.
- **Edit & Delete:** Full lifecycle management including status updates and deletions.

### 🚗 8. Travel Expenses
- **Reimbursement Monitoring:** Track travel expense claims submitted by field personnel.
- **Journey Audits:** Verify reported distance (km), transportation mode, and claim amounts against field visit records.
- **Detailed Expense Views:** Inspect bill attachments, purpose of journey, and approval status.

### 📐 9. Field Measurements
- **Land Survey Records:** View plot boundaries and land area measurements collected by field staff.
- **Area Calculation:** Accurate unit metrics (acres/cents/hectares) and perimeter assessments.
- **Crop Information:** Record crop types, plot notes, and geo-coordinates.

### 🐛 10. Pest Alerts & Crop Health
- **Infestation Monitoring:** Real-time logging of agricultural pest attacks and disease alerts.
- **Severity Levels:** Categorization by Low, Medium, High, and Critical alert levels.
- **Incident Management:** Add new alerts, assign affected zones, and delete resolved alerts.

### 📈 11. Reports & Analytics
- **Monthly Attendance Summaries:** Detailed breakdown of employee punctuality, working days, and deductions.
- **Filterable Time Periods:** View summaries by month and year.
- **Export Capabilities:** Prepare data for administrative reviews and payroll processing.

---

## 📁 Project Structure

```
admin-overview/
├── app.py                      # Main Flask application and API route controller
├── filters.py                  # Custom Jinja2 template filters and formatters
├── requirements.txt            # Python package dependencies
├── .env.example                # Template for environment configuration
├── .env                        # Local environment variables (kept private via .gitignore)
├── .gitignore                  # Git exclusions for secrets, credentials, and venvs
├── firebase-credentials.json   # Firebase service account private key (never committed)
├── setup.sh                    # Automated environment setup script
├── README.md                   # Project documentation
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css           # Custom styling and responsive UI rules
│   └── js/
│       └── main.js             # Client-side scripts and interactive UI helpers
│
└── templates/                  # Jinja2 HTML Templates
    ├── base.html               # Main layout wrapper and responsive navigation sidebar
    ├── login.html              # Authentication page
    ├── dashboard.html          # Main overview dashboard
    ├── employees.html          # Staff directory
    ├── add_employee.html       # Add new employee form
    ├── edit_employee.html      # Edit employee details
    ├── employee_detail.html    # Detailed employee history and profile
    ├── attendance.html         # Attendance logs and approval console
    ├── permissions.html        # Permission and leave requests
    ├── sessions.html           # Active and completed work sessions
    ├── session_detail.html     # Deep dive into session duration & photos
    ├── visits.html             # Field visits monitoring list
    ├── visit_detail.html       # Specific visit details and geo-information
    ├── tasks.html              # Task management overview
    ├── task_assign_field.html  # Field task assignment form
    ├── task_assign_office.html # Office task assignment form
    ├── task_detail.html        # Task view and status management
    ├── task_form.html          # Generic task create/edit template
    ├── travel_expenses.html    # Travel reimbursement claims list
    ├── travel_expense_detail.html # Individual travel expense breakdown
    ├── field_measurements.html # Land measurement list
    ├── field_measurement_detail.html # Plot details and survey record
    ├── pest_alerts.html        # Agricultural pest alerts dashboard
    ├── reports.html            # Attendance & analytics reports
    ├── 404.html                # Not found error page
    └── 500.html                # Server error page
```

---

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.8+**
- **pip** (Python package installer)
- **Firebase Project** with a Realtime Database enabled
- **Firebase Service Account Key** (`.json`)

### Step 1: Clone the Repository
```bash
git clone https://github.com/nscare62-maker/admin-overview.git
cd admin-overview
```

### Step 2: Create and Activate a Virtual Environment
```bash
# On Windows:
python -m venv .venv
.venv\Scripts\activate

# On Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Copy `.env.example` to create your `.env` file:
```bash
cp .env.example .env
```

Update `.env` with your settings:
```env
# Firebase Configuration
FIREBASE_DATABASE_URL=https://your-project-default-rtdb.firebaseio.com
FIREBASE_CREDENTIALS_PATH=firebase-credentials.json
AZURE_MAPS_SUBSCRIPTION_KEY=your-azure-maps-key-if-used

# Flask Configuration
FLASK_SECRET_KEY=generate-a-secure-random-secret-key
FLASK_ENV=development
FLASK_DEBUG=True

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123

# Server Binding
HOST=0.0.0.0
PORT=5000
```

### Step 5: Add Firebase Service Account Key
1. Go to **Firebase Console** → **Project Settings** → **Service Accounts**.
2. Click **Generate New Private Key**.
3. Save the downloaded file as `firebase-credentials.json` in the root of the project directory.

> 🔒 **Security Notice:** `firebase-credentials.json` and `.env` are included in `.gitignore` to prevent secret leakage.

### Step 6: Start the Application
```bash
python app.py
```
Open your browser and navigate to:
```
http://localhost:5000
```

---

## 🔐 Default Admin Credentials

| Field | Default Value | Note |
|---|---|---|
| **Username** | `admin` | Configurable in `.env` (`ADMIN_USERNAME`) |
| **Password** | `admin123` | Configurable in `.env` (`ADMIN_PASSWORD`) |

> ⚠️ **Important:** Change default credentials immediately before deploying to production!

---

## 🌐 Complete Route Map

### 🔐 Authentication
- `GET /login` - Admin login interface
- `POST /login` - Process admin authentication
- `GET /logout` - Clear session and sign out

### 📊 Dashboard & Analytics
- `GET /` or `GET /dashboard` - Central operations dashboard
- `GET /api/stats` - JSON endpoint for real-time KPI metrics

### 👥 Employees
- `GET /employees` - Directory of all staff members
- `GET /employees/add` & `POST /employees/add` - Add a new employee
- `GET /employees/<id>` - View employee profile and timeline
- `GET /employees/<id>/edit` & `POST /employees/<id>/edit` - Edit employee data
- `POST /employees/<id>/reset-password` - Reset employee password

### 📅 Attendance
- `GET /attendance` - Daily attendance records and filter
- `POST /attendance/<id>/approve` - Approve late start or half day
- `POST /attendance/<id>/reject` - Reject attendance variation

### 📝 Permissions & Leave
- `GET /permissions` - Review permission and leave requests
- `POST /permissions/<id>/approve` - Grant approval with manager remarks
- `POST /permissions/<id>/reject` - Reject permission with remarks

### ⏰ Work Sessions
- `GET /sessions` - Monitor live and historical work sessions
- `GET /sessions/<id>` - Detailed session view with duration breakdown & photos

### 📍 Field Visits
- `GET /visits` - Track on-ground visits with location filtering
- `GET /visits/<id>` - Deep dive into visit notes and GPS coordinates

### 📋 Task Management
- `GET /tasks` - Task board with status filters
- `GET /tasks/<id>` - Individual task overview
- `GET /tasks/assign/field` & `POST /tasks/assign/field` - Assign field tasks
- `GET /tasks/assign/office` & `POST /tasks/assign/office` - Assign office tasks
- `GET /tasks/<id>/edit` & `POST /tasks/<id>/edit` - Modify existing task
- `POST /tasks/<id>/status` - Update task progress state
- `POST /tasks/<id>/delete` - Remove a task

### 🚗 Travel Expenses
- `GET /travel-expenses` - Claims list with distance and amounts
- `GET /travel-expenses/<id>` - Detailed view of travel route & claim

### 📐 Field Measurements
- `GET /field-measurements` - Land survey records and calculated areas
- `GET /field-measurements/<id>` - Plot geometry, boundaries, and notes

### 🐛 Pest Alerts
- `GET /pest-alerts` - Pest incident monitor
- `POST /pest-alerts/add` - Log a new crop pest occurrence
- `POST /pest-alerts/<id>/delete` - Clear an alert

### 📈 Reports
- `GET /reports` - Monthly employee attendance and punctuality summaries

---

## 🔒 Security Architecture

1. **Session Protection:** Flask signed cookie sessions with configurable secret key.
2. **Access Control:** All operational routes are guarded by `@login_required`.
3. **Protected Credentials:** Private keys and configuration files are excluded via `.gitignore`.
4. **Production WSGI Ready:** Configured for high-concurrency production deployments with `gunicorn`.

---

## 🚀 Production Deployment

To run in production using Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📄 License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
