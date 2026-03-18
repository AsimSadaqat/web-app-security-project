# 🛡️ Web Application Security Project

## 📌 Overview
This project demonstrates a basic vulnerability assessment and security enhancement of a web application built using Flask.

The goal of this project was to:
- Identify common web vulnerabilities
- Exploit them for understanding
- Apply fixes to secure the application

---

## 🔍 Vulnerabilities Identified

- SQL Injection (Authentication Bypass)
- Cross-Site Scripting (XSS)
- Weak Password Storage
- Error-Based SQL Injection

---

## 🧪 Testing Performed

The following tests were conducted:

- Manual browser-based testing
- SQL Injection using:
  admin' OR '1'='1
- XSS testing using:
  <script>alert('XSS')</script>
- Database inspection using SQLite Viewer
- Basic penetration testing techniques

---

## 📸 Screenshots

### 🔹 User Interface (Login Page)
![UI](screenshots/3_ui_login_page.png)

---

### 🔹 User Registration Success
![Register](screenshots/2_user_registered_success.png)

---

### 🔹 Normal Login
![Login Success](screenshots/4_normal_login_success.png)

---

### 🔹 SQL Injection Attack
![SQL Injection](screenshots/7_sql_injection_success.png)

---

### 🔹 SQL Error (Error-Based Injection)
![SQL Error](screenshots/5_sql_error.png)

---

## 🛠️ Fixes Implemented

- Parameterized queries to prevent SQL Injection
- Password hashing using werkzeug.security
- Input sanitization using escape()
- Security headers using Flask-Talisman
- Logging system for monitoring events
- Input validation for user data

---

## 🧾 Logging

The application logs important events such as:
- User registration
- Login attempts (success and failure)
- Search queries

Logs are stored in:

security.log