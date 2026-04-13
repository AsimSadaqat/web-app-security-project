# 🔐 Week 6: Advanced Security Audits & Final Deployment

## 📌 Overview
In Week 6, advanced security testing and auditing were performed on the web application using multiple industry-standard tools.

---

## 🛠️ Tools Used
- OWASP ZAP
- Nikto
- Lynis

---

## 🔍 Security Audits Performed

### 🔹 OWASP ZAP
- Automated scan performed on the application
- Identified CSP issues and server header leaks

#### 📸 Screenshots
![ZAP Scan Start](Week6-Screenshots/ZAP/01_ZAP_Automated_Scan_Start.png)
![CSP Vulnerability](Week6-Screenshots/ZAP/02_ZAP_CSP_Vulnerability_Details.png)
![Server Header Leak](Week6-Screenshots/ZAP/03_ZAP_Server_Header_Leak.png)
![Alerts Details](Week6-Screenshots/ZAP/04_ZAP_Alerts_Details_View.png)

---

### 🔹 Nikto
- Scanned web server for vulnerabilities
- Found missing headers and exposed server info

#### 📸 Screenshots
![Nikto Scan](Week6-Screenshots/Nikto/01_Nikto_Scan_Result.png)

---

### 🔹 Lynis
- Performed system-level security audit
- Identified weak services and missing protections

#### 📸 Screenshots
![Initialization](Week6-Screenshots/Lynis/01_Lynis_Initialization.png)
![System Info](Week6-Screenshots/Lynis/02_Lynis_System_Info.png)
![Debian Tests](Week6-Screenshots/Lynis/03_Lynis_Debian_Tests.png)
![Services Analysis](Week6-Screenshots/Lynis/04_Lynis_Services_Analysis.png)
![Service Risks](Week6-Screenshots/Lynis/05_Lynis_Service_Risks.png)
![Kernel Checks](Week6-Screenshots/Lynis/06_Lynis_Kernel_Checks.png)
![User Authentication](Week6-Screenshots/Lynis/07_Lynis_Users_Authentication.png)
![File System Checks](Week6-Screenshots/Lynis/08_Lynis_File_System_Checks.png)
![USB Storage](Week6-Screenshots/Lynis/09_Lynis_USB_Storage.png)
![Network Services](Week6-Screenshots/Lynis/10_Lynis_Network_Services.png)

---

## 🚨 Key Findings
- Missing Content Security Policy (CSP)
- Server version information disclosure
- Missing X-Content-Type-Options header
- Unsafe system services
- Missing fail2ban (brute-force protection)

---

## 🔐 Security Improvements
- Implemented Content Security Policy (CSP)
- Removed sensitive server headers
- Disabled debug mode
- Added secure secret key handling
- Implemented rate limiting
- Identified system-level risks using Lynis

---

## 🧠 Conclusion
The application was successfully audited using multiple tools. Vulnerabilities were identified and mitigated, improving overall system security and aligning with OWASP Top 10 practices.

---