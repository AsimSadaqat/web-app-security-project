# 🛡️ Week 5: Ethical Hacking & Exploiting Vulnerabilities

## 📌 Objective
In this week, the goal was to perform ethical hacking techniques on the Flask web application, identify vulnerabilities, and implement security fixes.

---

## 🔍 1. Reconnaissance (Basic Testing)

Initial testing included exploring all available endpoints:

- Home Page
- Login Page
- Register Page
- API Endpoint (`/api/data`)

### 📸 Screenshots

#### 🏠 Home Page
![Home](screenshots/week-5/week5-home.png)

#### 🔐 Login Page
![Login](screenshots/week-5/week5-login.png)

#### 📝 Register Page
![Register](screenshots/week-5/week5-register.png)

---

## 💉 2. SQL Injection Testing (SQLMap)

### 🛠 Tool Used:
- SQLMap

### 💻 Command Used:
```bash
python sqlmap.py -u "http://127.0.0.1:5000/login" --data="username=test&password=test" --batch
