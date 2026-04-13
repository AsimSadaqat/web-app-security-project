# 🛡️ Week 6: Advanced Security Audit Report

## 📌 Overview
This report presents the results of security testing performed on the web application. Multiple tools were used to identify vulnerabilities and improve the security posture of the system.

---

## 🔍 Tools Used
- OWASP ZAP (Web Application Scanner)
- Nikto (Web Server Scanner)
- Lynis (System Security Audit Tool)

---

## 🚨 Vulnerabilities Identified

### 🔴 1. Missing Content Security Policy (CSP)
- **Tool:** OWASP ZAP  
- **Risk Level:** Medium  
- **Description:**  
  The application does not properly define a Content Security Policy (CSP), which may allow attackers to inject malicious scripts (XSS attacks).

- **Impact:**  
  Attackers may execute unauthorized scripts in the user’s browser.

- **Fix:**  
  Implement CSP using Flask-Talisman.

---

### 🟡 2. Server Information Disclosure
- **Tool:** OWASP ZAP  
- **Risk Level:** Low  
- **Description:**  
  The server exposes version details such as Werkzeug and Python in HTTP headers.

- **Impact:**  
  Attackers can use this information to identify known vulnerabilities.

- **Fix:**  
  Remove or modify the Server header in responses.

---

### 🟡 3. Missing X-Content-Type-Options Header
- **Tool:** Nikto  
- **Risk Level:** Low  
- **Description:**  
  The `X-Content-Type-Options` header is not set, allowing browsers to guess content types (MIME sniffing).

- **Impact:**  
  Can lead to incorrect content interpretation and security risks.

- **Fix:**  
  Add the header `X-Content-Type-Options: nosniff`.

---

### 🟡 4. Unsafe System Services
- **Tool:** Lynis  
- **Risk Level:** Medium  
- **Description:**  
  Several system services were marked as "UNSAFE", increasing the attack surface.

- **Impact:**  
  Unnecessary or insecure services may be exploited by attackers.

- **Fix:**  
  Disable or secure unnecessary services.

---

### 🟡 5. Missing Brute-Force Protection (fail2ban)
- **Tool:** Lynis  
- **Risk Level:** Medium  
- **Description:**  
  The system does not have fail2ban installed to protect against brute-force attacks.

- **Impact:**  
  Attackers can attempt unlimited login attempts.

- **Fix:**  
  Install fail2ban using:

  sudo apt install fail2ban

  
---

### 🟢 6. False Positive (WordPress File Detection)
- **Tool:** Nikto  
- **Risk Level:** Informational  
- **Description:**  
Nikto reported the presence of `/wp-config.php`, but the application is not using WordPress.

- **Impact:**  
No real impact.

- **Fix:**  
Ignore this result.

---

## 🛡️ OWASP Top 10 Compliance

- **A01 Broken Access Control** → Authentication and access controls implemented  
- **A02 Cryptographic Failures** → Password hashing used  
- **A03 Injection** → SQL Injection prevented using parameterized queries  
- **A05 Security Misconfiguration** → Security headers implemented  
- **A07 Identification and Authentication Failures** → Rate limiting and login protection applied  

---

## 🔐 Security Improvements Implemented
- Implemented Content Security Policy (CSP)
- Removed sensitive server headers
- Disabled debug mode
- Added secure secret key handling
- Implemented input validation and output escaping
- Enabled rate limiting for login attempts
- Identified system-level weaknesses using Lynis

---

## 🧠 Conclusion
The application was successfully tested using multiple security tools including OWASP ZAP, Nikto, and Lynis. Several vulnerabilities were identified and mitigated, improving the overall security posture of the system. The application now follows secure coding practices and is more resilient against common web attacks.

---