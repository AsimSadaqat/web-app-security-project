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
  The `X-Content-Type-Options` header is not set, allowing browsers to guess content types.

* **Impact:**
  Can lead to security risks.

* **Fix:**
  Add:

```
X-Content-Type-Options: nosniff
```

---

### 🟡 4. Unsafe System Services

* **Tool:** Lynis

* **Risk Level:** Medium

* **Description:**
  Several system services were marked as unsafe.

* **Impact:**
  Increases attack surface.

* **Fix:**
  Disable unnecessary services.

---

### 🟡 5. Missing Brute-Force Protection (fail2ban)

* **Tool:** Lynis

* **Risk Level:** Medium

* **Fix:**

```bash
sudo apt install fail2ban
```

---

### 🟢 6. False Positive (WordPress File Detection)

* **Tool:** Nikto

* **Risk Level:** Informational

* No real impact — safe to ignore.

---

## 📸 Evidence (Screenshots)

### 🔹 OWASP ZAP

![ZAP Scan](screenshots/week6/01_ZAP_Automated_Scan_Start.png)
![CSP Issue](screenshots/week6/02_ZAP_CSP_Vulnerability_Details.png)
![Server Leak](screenshots/week6/03_ZAP_Server_Header_Leak.png)
![Alerts](screenshots/week6/04_ZAP_Alerts_Details_View.png)

---

### 🔹 Nikto

![Nikto Scan](screenshots/week6/01_Nikto_Scan_Result.png)

---

### 🔹 Lynis

![Lynis Init](screenshots/week6/01_Lynis_Initialization.png)
![System Info](screenshots/week6/02_Lynis_System_Info.png)
![Debian Tests](screenshots/week6/03_Lynis_Debian_Tests.png)
![Services](screenshots/week6/04_Lynis_Services_Analysis.png)
![Service Risks](screenshots/week6/05_Lynis_Service_Risks.png)
![Kernel](screenshots/week6/06_Lynis_Kernel_Checks.png)
![Users](screenshots/week6/07_Lynis_Users_Authentication.png)
![Filesystem](screenshots/week6/08_Lynis_File_System_Checks.png)
![USB](screenshots/week6/09_Lynis_USB_Storage.png)
![Network](screenshots/week6/10_Lynis_Network_Services.png)

---

## 🔐 Security Improvements Implemented

* Implemented Content Security Policy (CSP)
* Removed sensitive server headers
* Disabled debug mode
* Added secure secret key handling
* Implemented input validation
* Enabled rate limiting
* Identified system risks using Lynis

---

## 🧠 Conclusion

The application was successfully tested using OWASP ZAP, Nikto, and Lynis.
Vulnerabilities were identified and mitigated, improving the overall security posture of the system.

---
