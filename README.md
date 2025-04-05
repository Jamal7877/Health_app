# Health_app
This repository contains all the necessary code to run the application on your device
# 🏥 Health Center Patient Management System

A web-based patient management system for a local health center built using **Python (Flask)** and **PostgreSQL**. This system allows for patient registration, appointment scheduling, and management of healthcare records through a secure and intuitive interface.

---

## 📌 Features

- ✅ User Authentication (Login Page)
- 📝 Patient Registration
- 📅 Appointment Booking
- 🗂️ Dashboard for navigation
- 💾 PostgreSQL Integration with SQLAlchemy
- 🌐 Responsive UI with HTML/CSS
- 🔐 Role-based functionality (Admin, Doctor)

---

## 🧱 Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (Jinja templating)
- **Database:** PostgreSQL (via SQLAlchemy ORM)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/health-center-app.git
cd health-center-app
# create a python virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
# install the dependencies
pip install -r requirements.txt
# configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/healthcare_db'
# FINALLY now run the app!!
python app.py
