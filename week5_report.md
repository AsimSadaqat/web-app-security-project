# 🛡️ Week 5: Ethical Hacking & Exploiting Vulnerabilities

## 📌 Objective
Perform ethical hacking on the Flask web app, test vulnerabilities, and apply security fixes.

---

## 🔍 1. Reconnaissance (Basic Testing)

Explored available endpoints:

- Home Page
- Login Page
- Register Page
- API Endpoint (`/api/data`)

---

## 📸 Screenshots

### 🏠 Home Page
![Home](../screenshots/week-5/week5-home.png)

### 🔐 Login Page
![Login](../screenshots/week-5/week5-login.png)

### 📝 Register Page
![Register](../screenshots/week-5/week5-register.png)

---

## 💉 2. SQL Injection Testing (SQLMap)

### 🛠 Tool Used:
- SQLMap

### 💻 Command:
```bash
python sqlmap.py -u "http://127.0.0.1:5000/login" --data="username=test&password=test" --batch
