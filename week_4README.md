# 🔐 Week 4: Security Hardening & Defensive Testing

## 📌 Overview

In Week 4, the application was enhanced with advanced security mechanisms to protect against common web attacks such as brute-force, unauthorized access, SQL Injection, and Cross-Site Scripting (XSS).

This phase focused on implementing defensive controls and validating them through testing.

---

## 🛡️ Security Features Implemented

### ⚡ 1. Rate Limiting

* Implemented using **Flask-Limiter**
* Limit set to **5 requests per minute**
* Protects against brute-force attacks

📸 Screenshot
![Rate Limit](screenshots/week4/week4-rate-limit.png)

---

### 🚫 2. Intrusion Detection (Account Lock)

* Tracks failed login attempts
* Locks account after 5 failed attempts

📸 Screenshots
![Account Lock Code](screenshots/week4/week4-account-lock-code%20\(6\).png)


---

### 🔐 3. API Security

* Protected API endpoint: `/api/data`
* Implemented API key authentication

#### 🔑 API Key

```text
x-api-key: secret123
```

#### Responses

* Unauthorized:

```json
{"error": "Unauthorized"}
```

* Authorized:

```json
{"message": "Secure API Access Granted"}
```

📸 Screenshots
![API Unauthorized](screenshots/week4/week4-api-unauthorized.png)
![API Authorized](screenshots/week4/week4-api-authorized.png)

---

### 🌐 4. CORS Configuration

* Restricted API access to:

```text
http://localhost:5000
```

* Prevents unauthorized cross-origin requests

---

### 🧱 5. Security Headers & CSP

* Implemented using **Flask-Talisman**
* Enabled:

  * HTTPS enforcement
  * HSTS
  * Content Security Policy (CSP)

---

## 🧪 Defensive Testing

### 😈 XSS Testing

Payload used:

```html
<script>alert(1)</script>
```

### Result:

* Rendered as plain text
* No JavaScript execution

📸 Screenshot
![XSS Protection](screenshots/week4/week4-xss-protection.png)

---

### 💉 SQL Injection Testing

Payload used:

```text
admin' OR '1'='1
```

### Result:

* Login failed
* Injection attempt blocked

📸 Screenshot
![SQL Injection Blocked](screenshots/week4/week4-sql-injection-blocked.png)

---

## 📊 Summary

| Security Feature | Status        |
| ---------------- | ------------- |
| Rate Limiting    | ✅ Implemented |
| Account Lock     | ✅ Working     |
| API Security     | ✅ Secured     |
| CORS             | ✅ Configured  |
| Security Headers | ✅ Enabled     |
| XSS Protection   | ✅ Tested      |
| SQL Injection    | ✅ Tested      |

---

## 🚀 Conclusion

Week 4 successfully strengthened the application by implementing multiple layers of security.
The system is now protected against common web vulnerabilities and demonstrates secure coding practices.






