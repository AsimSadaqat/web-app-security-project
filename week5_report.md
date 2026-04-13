# 🛡️ Week 5: Ethical Hacking & Exploiting Vulnerabilities

## 📌 Objective

The goal of Week 5 was to perform ethical hacking on the developed web application, identify vulnerabilities, exploit them in a controlled environment, and implement proper security defenses.

---

## 🔍 1. Application Overview

The target is a Flask-based web application with:

- User Registration
- Login System
- API Endpoint Protection
- Input Validation & Security Controls

---

## 🧪 2. Reconnaissance (Basic Testing)

Initial testing included exploring all available endpoints:

- Home Page
- Login Page
- Register Page
- API endpoints

### 📸 Screenshots

![Home Page](screenshots/week5-home.png)
![Login Page](screenshots/week5-login.png)
![Register Page](screenshots/week5-register.png)

---

## 💉 3. SQL Injection Testing (SQLMap)

### 🔧 Tool Used:
- SQLMap

### 🧪 Command Used:

```bash
python sqlmap.py -u "http://127.0.0.1:5000/login" --data="username=test&password=test" --batch