# 🛡️ Web Application Security Project

## 📌 Overview

This project demonstrates the identification, exploitation, and mitigation of common web application vulnerabilities using a Flask-based application.

The project is divided into multiple phases (Week 1–4), progressing from vulnerability discovery to implementing strong security defenses and testing them.

---

# 📅 Week 4: Security Hardening & Defensive Testing

In this phase, advanced security mechanisms were implemented to protect the application against real-world attacks such as brute-force, XSS, SQL Injection, and unauthorized API access.

---

## 🛡️ Security Features Implemented

### ⚡ Rate Limiting

* Implemented using **Flask-Limiter**
* Limit set to **5 requests per minute**
* Protects against brute-force login attempts

📸 Screenshot:

* `screenshots/week4/week4-rate-limit.png`

---

### 🚫 Intrusion Detection (Account Lock)

* Tracks failed login attempts
* Locks account after 5 failed attempts

📸 Screenshots:

* `screenshots/week4/week4-account-lock-code.png`
* `screenshots/week4/week4-account-lock-output.png`

---

### 🔐 API Security

* Protected endpoint: `/api/data`
* API key authentication implemented

#### API Key:

```
x-api-key: secret123
```

#### Responses:

* Unauthorized:

```
{"error": "Unauthorized"}
```

* Authorized:

```
{"message": "Secure API Access Granted"}
```

📸 Screenshots:

* `screenshots/week4/week4-api-unauthorized.png`
* `screenshots/week4/week4-api-authorized.png`

---

### 🌐 CORS Configuration

* Restricted API access to:

```
http://localhost:5000
```

* Prevents unauthorized cross-origin requests

---

### 🧱 Security Headers (CSP)

* Implemented using **Flask-Talisman**
* Enabled:

  * HTTPS enforcement
  * HSTS
  * Content Security Policy (CSP)

---

## 🧪 Defensive Testing

### 😈 XSS Testing

Payload used:

```
<script>alert(1)</script>
```

Result:

* Displayed as plain text
* No JavaScript execution occurred

📸 Screenshot:

* `screenshots/week4/week4-xss-protection.png`

---

### 💉 SQL Injection Testing

Payload used:

```
admin' OR '1'='1
```

Result:

* Login failed
* Injection attempt blocked

📸 Screenshot:

* `screenshots/week4/week4-sql-injection-blocked.png`

---

## 📊 Summary

| Security Feature       | Status        |
| ---------------------- | ------------- |
| Rate Limiting          | ✅ Implemented |
| Account Lock           | ✅ Working     |
| API Security           | ✅ Secured     |
| CORS                   | ✅ Configured  |
| Security Headers (CSP) | ✅ Enabled     |
| XSS Protection         | ✅ Tested      |
| SQL Injection          | ✅ Tested      |

---

## 🚀 Conclusion

Week 4 successfully enhanced the application by implementing multiple layers of security.
The system is now protected against common web vulnerabilities and follows secure coding practices.









