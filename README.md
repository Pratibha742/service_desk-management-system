# 🏢 Enterprise Service Desk  
### Issue & Change Management System (Backend)

An **enterprise-grade backend application** built using **Django REST Framework** to simulate how real IT organizations manage production issues, bug fixes, SLA breaches, and system changes.

This project follows **real-world backend development practices**, including RESTful APIs, authentication, role-based access control, structured workflows, and testing.

---

## 🎯 Project Objective

To design and develop a **scalable and secure service desk backend system** that mirrors how enterprise IT support teams handle:
- Production issues
- Issue severity & SLA tracking
- Role-based workflows
- Change management processes

---

## 🚀 Features Implemented

### 🔹 Issue Management
- Create, update, and track issues
- Severity-based classification:
  - Critical
  - High
  - Medium
  - Low
- SLA breach handling for high-priority issues

### 🔹 Issue Lifecycle Workflow
Structured enterprise workflow implemented:
Open → In Progress → Resolved → Closed


### 🔹 Authentication & Authorization
- JWT-based authentication
- Role-Based Access Control (RBAC)
- Secure API access based on user roles

### 🔹 Backend Architecture
- RESTful APIs using Django REST Framework
- Clean architecture with modular apps
- Django ORM with relational database design
- Soft delete support to prevent accidental data loss

### 🔹 Testing
- Unit tests written using `Django TestCase`
- APIs tested via:
  - DRF Browsable API
  - Postman

---

## 🛠 Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- JWT Authentication

### Database
- SQLite (Development)

### Tools & Practices
- REST / JSON APIs
- Git & GitHub
- Unit Testing
- Clean Architecture
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure
servicedesk/
├── accounts/ # Authentication & RBAC
├── issues/ # Issue management module
├── changes/ # Change request module (planned)
├── audits/ # Audit logs (planned)
├── servicedesk/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── README.md


---

## ✅ Current Status

- Core issue management module completed
- SLA breach logic implemented
- JWT authentication & RBAC implemented
- Issue lifecycle workflow fully functional
- Unit tests written and passing
- APIs stable and production-ready for core features

---

## 🔜 Planned Enhancements

- Background cron jobs for SLA monitoring
- Audit logging for compliance and traceability
- PostgreSQL database integration
- Deployment to production environment
- Change request management module

---

## ▶️ Getting Started (Local Setup)

### 1️⃣ Clone the Repository
```bash
git clone <https://github.com/Pratibha742>
cd servicedesk

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Start Development Server
python manage.py runserver

🧪 Run Tests
python manage.py test

📌 Why This Project?
This project demonstrates:
Real-world backend system design
Enterprise-style workflows
Secure API development
Testing and maintainable code practices
It is designed to showcase backend engineering skills relevant to Python/Django developer roles.

👩‍💻 Author

Pratibha Sharma
Backend Developer (Python | Django | DRF)

📌 GitHub: https://github.com/Pratibha742
📌 LinkedIn: www.linkedin.com/in/pratibha-sharma-749173285

⭐ If you find this project useful, feel free to star the repository!
- Pratibha Sharma
- https://github.com/Pratibha742/service_desk-management-system
- Github : https://github.com/Pratibha742

Add enterprise-level README documentation
