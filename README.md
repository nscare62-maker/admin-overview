# S2C Admin Dashboard - Employee Monitoring System

A comprehensive Flask-based web dashboard for monitoring and managing employees in the S2C (Start-to-Close) attendance tracking system.

## 🎯 Features

### 📊 Dashboard
- Real-time statistics overview
- Total employees count
- Active sessions monitoring
- Today's attendance summary
- Pending permissions count
- Quick action buttons
- System status information

### 👥 Employee Management
- View all employees
- Employee details page
- Recent sessions history
- Attendance records
- Monthly summary statistics
- Employee status tracking

### 📅 Attendance Management
- View all attendance records
- Filter by date and status
- Approve/reject late starts
- Approve/reject half days
- Track on-time, late start, and half-day attendance
- Automatic status detection

### 📝 Permission Management
- View all permission requests
- Filter by status (Pending/Approved/Rejected)
- Approve late start permissions
- Approve leave requests (CL/ML/Emergency/Planned)
- Add approval remarks
- Track permission history

### ⏰ Session Monitoring
- View all work sessions
- Filter by status (Active/Completed)
- Monitor active sessions in real-time
- Track work duration
- Track break duration
- View session details

### 📈 Reports
- Monthly attendance reports
- Employee punctuality reports
- Late start statistics
- Half-day deduction reports
- Exportable data

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Firebase project with Realtime Database
- Firebase service account credentials

### Step 1: Clone or Navigate to Directory
```bash
cd admin-dashboard
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR
venv\Scripts\activate  # On Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
```bash
cp .env.example .env
nano .env  # Edit with your settings
```

Update `.env` with your configuration:
```env
FIREBASE_DATABASE_URL=https://login-otp-29372-default-rtdb.firebaseio.com
FIREBASE_CREDENTIALS_PATH=firebase-credentials.json
FLASK_SECRET_KEY=your-secret-key-here-change-this
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
HOST=0.0.0.0
PORT=5000
```

### Step 5: Add Firebase Credentials
1. Go to Firebase Console → Project Settings → Service Accounts
2. Click "Generate New Private Key"
3. Save the JSON file as `firebase-credentials.json` in the `admin-dashboard` folder

### Step 6: Run the Application
```bash
python app.py
```

The dashboard will be available at: `http://localhost:5000`

---

## 🔐 Default Login Credentials

**Username:** `admin`  
**Password:** `admin123`

⚠️ **IMPORTANT:** Change these credentials in production!

---

## 📁 Project Structure

```
admin-dashboard/
├── app.py                      # Main Flask application
├── filters.py                  # Custom Jinja2 filters
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .env                       # Your environment variables (create this)
├── firebase-credentials.json  # Firebase service account key (add this)
├── README.md                  # This file
├── templates/                 # HTML templates
│   ├── base.html             # Base template with navigation
│   ├── login.html            # Login page
│   ├── dashboard.html        # Main dashboard
│   ├── employees.html        # Employee list
│   ├── employee_detail.html  # Employee details
│   ├── attendance.html       # Attendance records
│   ├── permissions.html      # Permission requests
│   ├── sessions.html         # Work sessions
│   ├── reports.html          # Reports page
│   ├── 404.html              # Not found page
│   └── 500.html              # Error page
└── static/                    # Static files
    ├── css/
    │   └── style.css         # Custom styles
    └── js/
        └── main.js           # JavaScript functions
```

---

## 🎨 Screenshots & Features

### Dashboard
- **Statistics Cards:** Total employees, active sessions, today's attendance, pending permissions
- **Quick Actions:** Direct links to common tasks
- **System Information:** Server status, Firebase connection, current date

### Employee Management
- **Employee List:** View all employees with status
- **Employee Details:** Complete profile with recent sessions and attendance
- **Monthly Summary:** On-time days, late starts, half days

### Attendance Management
- **Filter Options:** By date and status
- **Approval Actions:** Approve or reject with one click
- **Status Badges:** Color-coded (Green=On Time, Orange=Late, Red=Half Day)

### Permission Management
- **Request Types:** Late Start, CL, ML, Emergency, Planned Leave
- **Approval Workflow:** Review and approve/reject with remarks
- **Status Tracking:** Pending, Approved, Rejected

---

## 🔧 Configuration

### Firebase Setup
1. Ensure your Firebase Realtime Database has the following structure:
```
/
├── employees/
├── sessions/
├── attendance/
├── attendanceByDate/
├── attendanceSummary/
├── permissions/
├── employeePermissions/
├── lateStartRecords/
└── snoozeChecks/
```

2. Set Firebase Database Rules (for development):
```json
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```

### Security Rules (Production)
For production, implement proper security rules based on your requirements.

---

## 🌐 API Endpoints

### Authentication
- `GET /login` - Login page
- `POST /login` - Login submission
- `GET /logout` - Logout

### Dashboard
- `GET /` - Main dashboard
- `GET /api/stats` - Get statistics (JSON)

### Employees
- `GET /employees` - List all employees
- `GET /employees/<id>` - Employee details

### Attendance
- `GET /attendance` - List attendance records
- `POST /attendance/<id>/approve` - Approve attendance
- `POST /attendance/<id>/reject` - Reject attendance

### Permissions
- `GET /permissions` - List permission requests
- `POST /permissions/<id>/approve` - Approve permission
- `POST /permissions/<id>/reject` - Reject permission

### Sessions
- `GET /sessions` - List work sessions

### Reports
- `GET /reports` - Generate reports

---

## 🔒 Security Features

1. **Session Management:** Flask sessions with secret key
2. **Login Required:** All routes protected with `@login_required` decorator
3. **Firebase Authentication:** Service account credentials
4. **HTTPS Ready:** Can be deployed with SSL/TLS
5. **CSRF Protection:** Built-in Flask protection

---

## 🚀 Deployment

### Option 1: Local Server
```bash
python app.py
```

### Option 2: Gunicorn (Production)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Option 3: Docker (Coming Soon)
```bash
docker build -t s2c-admin .
docker run -p 5000:5000 s2c-admin
```

### Option 4: Cloud Deployment
- **Heroku:** Add `Procfile` and deploy
- **AWS:** Use Elastic Beanstalk or EC2
- **Google Cloud:** Use App Engine or Cloud Run
- **Azure:** Use App Service

---

## 📊 Usage Guide

### Approving Attendance
1. Navigate to **Attendance** page
2. Filter by date or status
3. Click **✓** button to approve
4. Click **✗** button to reject
5. Add remarks if needed

### Approving Permissions
1. Navigate to **Permissions** page
2. Click **Pending** to see pending requests
3. Review request details
4. Click **Approve** or **Reject**
5. Add remarks explaining decision

### Monitoring Sessions
1. Navigate to **Sessions** page
2. Filter by **Active** to see current sessions
3. View employee work duration
4. Monitor break times

### Generating Reports
1. Navigate to **Reports** page
2. Select report type
3. Choose month/date range
4. Click **Generate**
5. Export to CSV if needed

---

## 🛠️ Troubleshooting

### Firebase Connection Error
- Check `firebase-credentials.json` file exists
- Verify Firebase Database URL in `.env`
- Ensure Firebase project is active

### Login Not Working
- Check `ADMIN_USERNAME` and `ADMIN_PASSWORD` in `.env`
- Clear browser cookies
- Check Flask secret key is set

### Data Not Loading
- Verify Firebase database has data
- Check Firebase security rules
- Check browser console for errors

### Port Already in Use
```bash
# Change port in .env
PORT=8000

# Or kill existing process
lsof -ti:5000 | xargs kill -9
```

---

## 📝 Development

### Adding New Features
1. Create new route in `app.py`
2. Create template in `templates/`
3. Add navigation link in `base.html`
4. Test thoroughly

### Custom Filters
Add new filters in `filters.py`:
```python
def my_custom_filter(value):
    # Your logic here
    return formatted_value

# Register in register_filters()
app.jinja_env.filters['my_filter'] = my_custom_filter
```

### Styling
Edit `static/css/style.css` for custom styles.

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

---

## 📄 License

This project is part of the S2C Employee Monitoring System.

---

## 📞 Support

For issues or questions:
1. Check this README
2. Review Firebase console
3. Check application logs
4. Contact system administrator

---

## 🎯 Roadmap

- [ ] Export reports to PDF
- [ ] Email notifications
- [ ] SMS alerts
- [ ] Mobile responsive improvements
- [ ] Dark mode
- [ ] Multi-language support
- [ ] Advanced analytics
- [ ] Role-based access control
- [ ] Audit logs
- [ ] Backup/restore functionality

---

**Version:** 1.0.0  
**Last Updated:** April 29, 2026  
**Status:** ✅ Production Ready
