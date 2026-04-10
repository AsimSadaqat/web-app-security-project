# 🛡️ Web Application Security Assessment Report

---

# 📌 1. Overview

This project focuses on identifying, exploiting, and securing common vulnerabilities in a Flask-based web application.
The goal was to understand real-world web security issues and implement defensive mechanisms to protect the application.

The project was completed in multiple phases (Week 1–4), starting from vulnerability discovery to implementing strong security controls and testing them.

---

# 🔍 2. Week 1–2: Vulnerability Identification

During the initial phase, the application was tested for common security flaws.

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

This phase focused on advanced security controls and testing.

---

## ⚡ Rate Limiting

* Implemented using **Flask-Limiter**
* Limit: **5 requests per minute**

**Result:**

* Prevents brute-force attacks
* Returns:

```
Too Many Requests
```

📸 Evidence:

* week4-rate-limit.png

---

## 🚫 Intrusion Detection (Account Lock)

* Tracks failed login attempts
* Locks account after 5 failures

**Result:**

```
Account temporarily locked due to multiple failed attempts
```

📸 Evidence:

* week4-account-lock-code.png
* week4-account
