# 🛡️ Web Application Security Assessment Report

---

## 📌 1. Overview

This project demonstrates the identification, exploitation, and mitigation of common web application vulnerabilities in a Flask-based application.

The assessment was conducted in multiple phases (Week 1–6), progressing from vulnerability discovery to implementing strong security controls and performing advanced security audits.

---

## 🔍 2. Week 1–2: Vulnerability Identification

### 🔴 SQL Injection

**Payload:**

```
admin' OR '1'='1
```

**Impact:**

* Authentication bypass
* Unauthorized access

---

### 🔴 Cross-Site Scripting (XSS)

**Payload:**

```
<script>alert('XSS')</script>
```

**Impact:**

* Malicious script execution
* Session hijacking

---

### 🔴 Weak Password Storage

**Impact:**

* Credential exposure
* Full account compromise

---

### 🔴 Error-Based SQL Injection

**Impact:**

* Information disclosure
* Database structure exposure

---

## 🧪 3. Week 3: Testing & Exploitation

Performed:

* Manual testing
* SQL Injection attacks
* XSS execution
* SQLite inspection
* OWASP ZAP scanning

✅ Result: Application confirmed vulnerable

---

## 🛠️ 4. Week 3: Fixes Implemented

### 🔐 Security Controls

* Parameterized queries (SQL Injection prevention)
* Password hashing (`generate_password_hash`)
* Output escaping (`escape()`)
* Input validation
* Secure error handling

---

## 🛡️ 5. Week 4: Security Hardening

### ⚡ Rate Limiting

![Rate Limit](screenshots/week4/week4-rate-limit.png)

---

### 🚫 Account Lock (Intrusion Detection)

![Account Lock](screenshots/week4/week4-account-lock-code.png)

---

### 🔐 API Security

![Authorized](screenshots/week4/week4-api-authorized.png)
![Unauthorized](screenshots/week4/week4-api-unauthorized.png)

---

### 🧱 Additional Protections

![SQL Injection Blocked](screenshots/week4/week4-sql-injection-blocked.png)
![XSS Protection](screenshots/week4/week4-xss-protection.png)

---

## 🗓️ 6. Week 5: Ethical Hacking

### 📸 Application Screens

![Home](screenshots/week5/week5-home.png)
![Login](screenshots/week5/week5-login.png)
![Register](screenshots/week5/week5-register.png)

---

### 💉 SQLMap Testing

```bash
python sqlmap.py -u "http://127.0.0.1:5000/login" --data="username=test&password=test" --batch
```

📸 Evidence
![SQLMap 1](screenshots/week5/week5-sqlmap-result-part1.png)
![SQLMap 2](screenshots/week5/week5-sqlmap-result-part2.png)

---

## 📅 7. Week 6: Advanced Security Audits

### 🛠️ Tools Used

* OWASP ZAP
* Nikto
* Lynis

---

### 🔍 Key Findings

* Missing Content Security Policy (CSP)
* Server information leakage
* Missing security headers
* Unsafe system services
* No brute-force protection (fail2ban)

---

### 🔐 Improvements Implemented

* CSP enabled
* Sensitive headers removed
* Debug mode disabled
* Input validation strengthened
* Rate limiting enforced
* System audit performed using Lynis

---

### 📸 Evidence

#### OWASP ZAP

![ZAP](screenshots/week6/01_ZAP_Automated_Scan_Start.png)
![CSP](screenshots/week6/02_ZAP_CSP_Vulnerability_Details.png)

#### Nikto

![Nikto](screenshots/week6/01_Nikto_Scan_Result.png)

#### Lynis

![Lynis](screenshots/week6/01_Lynis_Initialization.png)

---

## 🧠 8. Key Learnings

* Practical exploitation of real-world vulnerabilities
* Secure coding practices implementation
* Defense-in-depth strategy
* Security auditing using industry tools

---

## 🚀 9. Conclusion

This project demonstrates a complete **offensive + defensive security lifecycle**:

* 🔍 Vulnerability discovery
* 💉 Exploitation
* 🔐 Mitigation
* 🛡️ Hardening
* 🔎 Security auditing

The application evolved into a secure, production-ready system aligned with **OWASP Top 10 standards**.

---
