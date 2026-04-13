# 🛡️ Web Application Security Assessment Report

---

# 📌 1. Overview

This project focuses on identifying, exploiting, and securing common vulnerabilities in a Flask-based web application.
The goal was to understand real-world web security issues and implement defensive mechanisms to protect the application.

The project was completed in multiple phases (Week 1–5), starting from vulnerability discovery to implementing strong security controls and testing them.

---

# 🔍 2. Week 1–2: Vulnerability Identification

## 🔴 SQL Injection

The login system was vulnerable to SQL Injection.

**Payload used:**

```
admin' OR '1'='1
```

**Impact:**

* Authentication bypass
* Unauthorized access

---

## 🔴 Cross-Site Scripting (XSS)

User input was not sanitized, allowing script execution.

**Payload used:**

```
<script>alert('XSS')</script>
```

**Impact:**

* Execution of malicious scripts
* Session hijacking risk

---

## 🔴 Weak Password Storage

Passwords were stored in plain text.

**Impact:**

* Easy credential theft
* Full account compromise

---

## 🔴 Error-Based SQL Injection

Application exposed database errors.

**Impact:**

* Information leakage
* Helps attackers map database

---

# 🧪 3. Week 3: Testing & Exploitation

The vulnerabilities were tested using:

* Manual browser testing
* SQL Injection attacks
* XSS payload execution
* Database inspection (SQLite)
* Optional OWASP ZAP scanning

These tests confirmed that the application was vulnerable and exploitable.

---

# 🛠️ 4. Week 3: Fixes Implemented

## 🔐 SQL Injection Prevention

* Replaced raw queries with parameterized queries

## 🔐 Password Security

* Implemented hashing using:

  * `generate_password_hash()`
  * `check_password_hash()`

## 🔐 XSS Protection

* Used:

  * `escape()` from markupsafe

## 🔐 Input Validation

* Enforced minimum username/password length

## 🔐 Error Handling

* Prevented database error exposure

---

# 🛡️ 5. Week 4: Security Hardening & Defensive Testing

## ⚡ Rate Limiting

* Implemented using **Flask-Limiter**
* Limit: **5 requests per minute**

**Result:**

* Prevents brute-force attacks
* Returns: `Too Many Requests`

### 📸 Evidence

![Rate Limit](screenshots/week4/week4-rate-limit.png)

---

## 🚫 Intrusion Detection (Account Lock)

* Tracks failed login attempts
* Locks account after 5 failures

**Result:**

```
Account temporarily locked due to multiple failed attempts
```

### 📸 Evidence

![Account Lock](screenshots/week4/week4-account-lock-code.png)

---

## 🔐 Additional Protections

### API Authorization

![Authorized](screenshots/week4/week4-api-authorized.png)
![Unauthorized](screenshots/week4/week4-api-unauthorized.png)

---

### SQL Injection Protection

![SQL Injection Blocked](screenshots/week4/week4-sql-injection-blocked.png)

---

### XSS Protection

![XSS Protection](screenshots/week4/week4-xss-protection.png)

---

# 🗓️ 6. Week 5: Ethical Hacking & Exploiting Vulnerabilities

## 🎯 Objective

The objective of Week 5 was to perform ethical hacking on the developed web application, identify potential vulnerabilities, exploit them in a controlled environment, and implement proper security measures.

---

## 🔍 6.1 Reconnaissance & Application Analysis

The application was analyzed to identify attack surfaces:

* Home Page
* Login System
* Registration Form
* API Endpoints

### 📸 Screenshots

![Home Page](screenshots/week5/week5-home.png)
![Login Page](screenshots/week5/week5-login.png)
![Register Page](screenshots/week5/week5-register.png)

---

## 💉 6.2 SQL Injection Testing (SQLMap)

SQL Injection testing was performed using SQLMap.

### 🔧 Command Used:

```bash
python sqlmap.py -u "http://127.0.0.1:5000/login" --data="username=test&password=test" --batch
```

### 📸 Evidence

![SQLMap Result 1](screenshots/week5/week5-sqlmap-result-part1.png)
![SQLMap Result 2](screenshots/week5/week5-sqlmap-result-part2.png)

---

# 🛡️ 7. Conclusion

This project demonstrated how common web vulnerabilities can be identified, exploited, and mitigated.

### ✅ Key Learnings:

* Importance of input validation
* Secure password storage
* Protection against SQL Injection & XSS
* Implementation of rate limiting and intrusion detection

The application evolved from a vulnerable system to a more secure and production-ready application.
