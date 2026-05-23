# 🌾 AgroConnect — APMC Online Portal

> A modern web-based Agricultural Produce Market Committee (APMC) portal that connects **farmers** and **administrators** — enabling crop management, transport booking, price tracking, and complaint resolution in one place.

---

## 📸 Screenshots

| Admin Dashboard | User Dashboard |
|---|---|
| ![Admin Dashboard](base/docs/admin_dashboard.png) | ![User Dashboard](base/docs/user_dashboard.png) |


---

## ✨ Features

### 👨‍💼 Admin Portal
- 📊 Live dashboard with stats — users, crop requests, transport, complaints
- 👥 View and manage all registered farmers/users
- 🌱 Review and approve/reject crop requests
- 🚛 Monitor transport requests
- 📅 Manage time slots and bookings
- 💰 Update market price chart for crops
- 💬 View and reply to complaints
- ⭐ Review farmer feedback & ratings
- 🚗 Manage vehicle catalogue

### 👨‍🌾 User (Farmer) Portal
- 📊 Personal dashboard — my requests, bookings, complaints
- 🌱 Submit crop requests (type, name, quantity)
- 🚛 Request transport for crop delivery
- 📅 Browse & book available time slots
- 💰 View live market prices for crops
- 💬 Raise and track complaints
- ⭐ Submit feedback & ratings
- 👤 View personal profile

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Architecture** | MVC — DAO / VO / Controller |
| **Frontend** | HTML, CSS, Bootstrap 4, JavaScript (Fetch API) |
| **Auth** | Flask Session-based login |
| **UI Theme** | AdminLTE / Custom light theme |

---

## 📁 Project Structure

```
base/
├── __init__.py                  # App factory, db init
├── com/
│   ├── controller/
│   │   ├── login_controller.py
│   │   ├── crop_controller.py
│   │   ├── booking_controller.py
│   │   ├── dashboard_controller.py  ← Dashboard API routes
│   │   └── ...
│   ├── dao/
│   │   ├── crop_dao.py
│   │   ├── dashboard_dao.py         ← Dashboard ORM queries
│   │   └── ...
│   └── vo/
│       ├── crop_vo.py               ← SQLAlchemy models (untouched)
│       ├── login_vo.py
│       └── ...
templates/
├── admin/
│   ├── index.html                   ← Admin dashboard
│   ├── header.html
│   ├── menu.html
│   └── footer.html
└── user/
    ├── index.html                   ← User dashboard
    ├── header.html
    ├── menu.html
    └── footer.html
static/
└── adminResources/
    ├── css/
    ├── js/
    └── images/
app.py
requirements.txt
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- pip

### 1. Clone the repository

```bash
git clone https://github.com/swapnil-patel-21/apmc-online-portal.git
cd apmc-online-portal
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Create a PostgreSQL database:

```sql
CREATE DATABASE projectdb;
```

Update your database config in `base/__init__.py` or your config file:

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/projectdb'
```

### 5. Import the database schema

```bash
psql -U postgres -d projectdb -f projectdb.sql
```

<!-- > Or use Flask-Migrate if configured:
> ```bash
> flask db upgrade
> ``` -->

### 6. Run the application

```bash
python run.py
```

Open your browser at **http://localhost:5000**

<!-- ---

## 🔐 Default Login Credentials

| Role | Username | Password |
|---|---|---|
| Admin | `admin` | `admin123` |
| User | `farmer1` | `user123` |

> ⚠️ Change these credentials immediately after first login in production.

--- -->

## 🗄️ Database Schema

| Table | Description |
|---|---|
| `login_table` | Auth credentials and roles |
| `user_table` | Farmer/user profile details |
| `crop_table` | Crop type catalogue |
| `crop_name_table` | Crop name & description |
| `croprequest_table` | Farmer crop submissions |
| `price_chart_table` | Daily market prices per crop |
| `timeslot_table` | Available booking slots |
| `booking_table` | Slot bookings by farmers |
| `transportrequest_table` | Vehicle transport requests |
| `vehicle_table` | Registered vehicles |
| `complain_table` | Complaints with replies |
| `feedback_table` | Farmer ratings & feedback |

---

<!-- ## 🔌 Dashboard API Endpoints -->

All endpoints are session-protected. 404 if not logged in.

### Admin (`/admin/dashboard/*`)

| Method | Endpoint | Description |
|---|---|---|
| GET | `/admin/dashboard` | Render admin dashboard page |
| GET | `/admin/dashboard/stats` | Platform-wide counts & averages |
| GET | `/admin/dashboard/crop_requests` | Recent 6 crop requests |
| GET | `/admin/dashboard/transport_requests` | Recent 5 transport requests |
| GET | `/admin/dashboard/complaints` | Recent 5 complaints |
| GET | `/admin/dashboard/price_chart` | Latest 6 crop prices |
| GET | `/admin/dashboard/users` | Recent 6 registered users |
| GET | `/admin/dashboard/feedback` | Recent 5 feedback entries |

### User (`/user/dashboard/*`)

| Method | Endpoint | Description |
|---|---|---|
| GET | `/user/dashboard` | Render user dashboard page |
| GET | `/user/dashboard/stats` | My activity counts |
| GET | `/user/dashboard/crop_requests` | My crop requests |
| GET | `/user/dashboard/transport_requests` | My transport requests |
| GET | `/user/dashboard/bookings` | My bookings |
| GET | `/user/dashboard/complaints` | My complaints |
| GET | `/user/dashboard/price_chart` | Current market prices |
| GET | `/user/dashboard/slots` | Available upcoming slots |
| GET | `/user/dashboard/profile` | My profile info |

---

## 🏗️ MVC Architecture

```
HTTP Request
     │
     ▼
Controller (dashboard_controller.py)
  - Checks session role
  - Calls DAO method
  - Returns jsonify() response
     │
     ▼
DAO (dashboard_dao.py)
  - SQLAlchemy ORM queries
  - Joins VOs (models)
  - Returns plain dict list
     │
     ▼
VO (existing *_vo.py files)
  - SQLAlchemy model definitions
  - Not modified
```

---

## 📦 Requirements

```
Flask
Flask-SQLAlchemy
psycopg2-binary
SQLAlchemy
Werkzeug
...
```

Full list in `requirements.txt`.

<!-- ---

## 🚀 Deployment Notes

- Set `DEBUG = False` in production
- Use **Gunicorn** as the WSGI server:
  ```bash
  gunicorn -w 4 run:app
  ```
- Use **Nginx** as a reverse proxy
- Store secrets in environment variables, not in code

--- -->

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: swapnil-patel-21 (https://github.com/swapnil-patel-21)
<!-- - Email: your-email@example.com -->

---

<p align="center">Made with ❤️ for farmers 🌾</p>