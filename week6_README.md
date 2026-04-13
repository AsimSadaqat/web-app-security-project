# 🔐 Week 6: Advanced Security Audits & Final Deployment

## 📌 Overview

In Week 6, advanced security testing and auditing were performed on the web application using multiple industry-standard tools.

---

## 🛠️ Tools Used

* OWASP ZAP
* Nikto
* Lynis

---

## 🔍 Security Audits Performed

### 🔹 OWASP ZAP

* Automated scan performed on the application
* Identified CSP issues and server header leaks

#### 📸 Screenshots

![ZAP Scan Start](screenshots/week6/01_ZAP_Automated_Scan_Start.png)
![CSP Vulnerability](screenshots/week6/02_ZAP_CSP_Vulnerability_Details.png)
![Server Header Leak](screenshots/week6/03_ZAP_Server_Header_Leak.png)
![Alerts Details](screenshots/week6/04_ZAP_Alerts_Details_View.png)

---

### 🔹 Nikto

* Scanned web server for vulnerabilities
* Found missing headers and exposed server info

#### 📸 Screenshots

![Nikto Scan](screenshots/week6/01_Nikto_Scan_Result.png)

---

### 🔹 Lynis

* Performed system-level security audit
* Identified weak services and missing protections

#### 📸 Screenshots

![Initialization](screenshots/week6/01_Lynis_Initialization.png)
![System Info](screenshots/week6/02_Lynis_System_Info.png)
![Debian Tests](screenshots/week6/03_Lynis_Debian_Tests.png)
![Services Analysis](screenshots/week6/04_Lynis_Services_Analysis.png)
![Service Risks](screenshots/week6/05_Lynis_Service_Risks.png)
![Kernel Checks](screenshots/week6/06_Lynis_Kernel_Checks.png)
![User Authentication](screenshots/week6/07_Lynis_Users_Authentication.png)
![File System Checks](screenshots/week6/08_Lynis_File_System_Checks.png)
![USB Storage](screenshots/week6/09_Lynis_USB_Storage.png)
![Network Services](screenshots/week6/10_Lynis_Network_Services.png)

---

## 🚨 Key Findings

* Missing Content Security Policy (CSP)
* Server version information disclosure
* Missing X-Content-Type-Options header
* Unsafe system services
* Missing fail2ban (brute-force protection)

---

## 🔐 Security Improvements

* Implemented Content Security Policy (CSP)
* Removed sensitive server headers
* Disabled debug mode
* Added secure secret key handling
* Implemented rate limiting
* Identified system-level risks using Lynis

---

## 🧠 Conclusion

The application was successfully audited using multiple tools. Vulnerabilities were identified and mitigated, improving overall system security and aligning with OWASP Top 10 practices.

---


