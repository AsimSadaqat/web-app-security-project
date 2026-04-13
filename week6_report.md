# 🛡️ Week 6: Advanced Security Audit Report

## 📌 Overview

This report presents the results of security testing performed on the web application. Multiple tools were used to identify vulnerabilities and improve the security posture of the system.

---

## 🔍 Tools Used

* OWASP ZAP (Web Application Scanner)
* Nikto (Web Server Scanner)
* Lynis (System Security Audit Tool)

---

## 🚨 Vulnerabilities Identified

### 🔴 1. Missing Content Security Policy (CSP)

* **Tool:** OWASP ZAP

* **Risk Level:** Medium

* **Description:**
  The application does not properly define a Content Security Policy (CSP), which may allow attackers to inject malicious scripts (XSS attacks).

* **Impact:**
  Attackers may execute unauthorized scripts in the user’s browser.

* **Fix:**
  Implement CSP using Flask-Talisman.

---

### 🟡 2. Server Information Disclosure

* **Tool:** OWASP ZAP

* **Risk Level:** Low

* **Description:**
  The server exposes version details such as Werkzeug and Python in HTTP headers.

* **Impact:**
  Attackers can use this information to identify known vulnerabilities.

* **Fix:**
  Remove or modify the Server header in responses.

---

### 🟡 3. Missing X-Content-Type-Options Header

* **Tool:** Nikto

* **Risk Level:** Low

* **Description:**
  The `X-Content-Type-Options` header is not set, allowing browsers to guess content types (MIME sniffing).

* **Impact:**
  Can lead to incorrect content interpretation and security risks.

* **Fix:**
  Add the header `X-Content-Type-Options: nosniff`.

---

### 🟡 4. Unsafe System Services

* **Tool:** Lynis

* **Risk Level:** Medium

* **Description:**
  Several system services were marked as "UNSAFE", increasing the attack surface.

* **Impact:**
  Unnecessary or insecure services may be exploited by attackers.

* **Fix:**
  Disable or secure unnecessary services.

---

### 🟡 5. Missing Brute-Force Protection (fail2ban)

* **Tool:** Lynis

* **Risk Level:** Medium

* **Description:**
  The system does not have fail2ban installed to protect against brute-force attacks.

* **Impact:**
  Attackers can attempt unlimited login attempts.

* **Fix:**
  Install fail2ban using:

  sudo apt install fail2ban

---

### 🟢 6. False Positive (WordPress File Detection)

* **Tool:** Nikto

* **Risk Level:** Informational

* **Description:**
  Nikto reported the presence of `/wp-config.php`, but the application is not using WordPress.

* **Impact:**
  No real impact.

* **Fix:**
  Ignore this result.

---

## 🛡️ OWASP Top 10 Mapping

The identified vulnerabilities were mapped to OWASP Top 10 categories:

* **A05: Security Misconfiguration**

  * Missing Content Security Policy (CSP)
  * Missing security headers (X-Content-Type-Options)
  * Exposure of server version information

* **A02: Cryptographic Failures**

  * Weak or missing system-level protections (Lynis findings)

* **A03: Injection**

  * Previously tested in earlier phases (Week 1–3)

* **A07: Identification and Authentication Failures**

  * Missing brute-force protection (fail2ban not installed)

* **A09: Security Logging and Monitoring Failures**

  * Limited monitoring and alerting mechanisms

---

## 🚀 Secure Deployment Practices

The following secure deployment measures were considered:

* Enabled system updates using:
  sudo apt update && sudo apt upgrade

* Recommended dependency and vulnerability scanning tools:

  * pip-audit
  * safety

* Suggested container security practices:

  * Scan Docker images using tools like Trivy
  * Avoid running containers as root
  * Use minimal base images

* Followed least privilege principle for system services

* Identified missing protections (fail2ban) and recommended installation

---

## 📸 Evidence (Screenshots)

### 🔹 OWASP ZAP

![ZAP Scan](Week6-Screenshots/ZAP/01_ZAP_Automated_Scan_Start.png)
![CSP Issue](Week6-Screenshots/ZAP/02_ZAP_CSP_Vulnerability_Details.png)
![Server Leak](Week6-Screenshots/ZAP/03_ZAP_Server_Header_Leak.png)
![Alerts](Week6-Screenshots/ZAP/04_ZAP_Alerts_Details_View.png)

### 🔹 Nikto

![Nikto Scan](Week6-Screenshots/Nikto/01_Nikto_Scan_Result.png)

### 🔹 Lynis

![Lynis Init](Week6-Screenshots/Lynis/01_Lynis_Initialization.png)
![System Info](Week6-Screenshots/Lynis/02_Lynis_System_Info.png)
![Debian Tests](Week6-Screenshots/Lynis/03_Lynis_Debian_Tests.png)
![Services](Week6-Screenshots/Lynis/04_Lynis_Services_Analysis.png)
![Service Risks](Week6-Screenshots/Lynis/05_Lynis_Service_Risks.png)
![Kernel](Week6-Screenshots/Lynis/06_Lynis_Kernel_Checks.png)
![Users](Week6-Screenshots/Lynis/07_Lynis_Users_Authentication.png)
![Filesystem](Week6-Screenshots/Lynis/08_Lynis_File_System_Checks.png)
![USB](Week6-Screenshots/Lynis/09_Lynis_USB_Storage.png)
![Network](Week6-Screenshots/Lynis/10_Lynis_Network_Services.png)

---

## 🔐 Security Improvements Implemented

* Implemented Content Security Policy (CSP)
* Removed sensitive server headers
* Disabled debug mode
* Added secure secret key handling
* Implemented input validation and output escaping
* Enabled rate limiting for login attempts
* Identified system-level weaknesses using Lynis

---

## 🧠 Conclusion

The application was successfully tested using multiple security tools including OWASP ZAP, Nikto, and Lynis. Several vulnerabilities were identified and mitigated, improving the overall security posture of the system. The application now follows secure coding practices and is more resilient against common web attacks.

---
