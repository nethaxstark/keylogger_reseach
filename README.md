# **🛠️ Advanced Keylogger Tool - Comprehensive Project Overview**  
*(Strictly for Educational and Research Purposes)*  

---

## **🌐 Project Overview**  
This **Python-based Keylogger** is a sophisticated monitoring tool designed to demonstrate system input tracking, data persistence, and covert communication techniques. The project implements multiple advanced features while maintaining clean, modular code architecture.

```mermaid
graph TD
    A[Keylogger Project] --> B[Offensive Skills]
    A --> C[Defensive Skills]
    B --> B1(Memory/Process Manipulation)
    B --> B2(Data Exfiltration)
    C --> C1(Log Analysis)
    C --> C2(Detection Rules)
    C --> C3(Incident Response)
```

---

## **📜 Detailed Code Structure Breakdown**

```python
📂 keylogger_research
├── 📂 src/📜 keylogger_mail.py (Main executable)
├── 📂 docs/
│   ├── analysis.md (analysis.doc)
│   └── detection.md (detection.doc)
├── 📂 samples/
│   ├── sample_keyloggermail.pcapng (pcapng Wireshark)
│   └── sample_keylogs.txt (sample keylogs)
└── 📜 README.md (Project documentation)
```

---

## 🎥 Demo  
### Python Execution  
![Python Code Running](https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif)  

### Email Reporting  
![SMTP Working](https://media.giphy.com/media/5WJ6K7XnP2K2p3VWft/giphy.gif)  

## ⚠️ Legal Notice  
![Warning](https://media.giphy.com/media/3ohhwM5vJwkb2N13Fe/giphy.gif)  

## **⚙️ Enhanced Feature Set**

### **🔍 Core Logging System**
- **Real-time Keystroke Capture** using `pynput`'s asynchronous listener
- **Context-Aware Logging**:
  - Distinguishes between:
    - Alphanumeric characters (`key.char`)
    - Modifier keys (Shift/Ctrl/Alt)
    - Special keys (Enter, Tab, Backspace)
  - Maintains temporal sequence with microsecond precision

### **🔄 Intelligent Log Management**
```python
def check_log_size():
    """Implements a rolling log system with:
    - Size-based rotation (1MB threshold)
    - Time-based archiving (YYYYMMDD_HHMMSS format)
    - Atomic file operations (os.rename)"""
```

### **📧 Stealthy Data Exfiltration**
- **SMTP Email Channel**:
  - MIME-compliant message formatting
  - Base64-encoded attachments
  - Local SMTP fallback (localhost:1025)
- **Content Preview System**:
  - Partial log decoding (first 500 chars)
  - Binary data safety checks

### **🔐 Data Obfuscation Layer**
```python
def decode_base64_logs(encoded_data):
    """Advanced Base64 handler with:
    - Automatic padding correction
    - Multi-encoding detection (UTF-8/ASCII/binary)
    - Regex-based payload extraction
    - Error-resistant decoding"""
```

---

## **🛡️ Anti-Detection Mechanisms**

1. **Low-Resource Design**
   - Event-driven architecture (no polling)
   - Minimal memory footprint (<5MB)
   - Buffered file I/O operations

2. **Operational Security**
   - No persistent registry changes
   - Clean log file handling
   - Local testing configuration by default

3. **Plausible Deniability**
   - Educational-purpose comments
   - Explicit warning messages
   - No auto-start mechanisms

---

## **📊 Technical Specifications**

| Component          | Technology Used             | Purpose                          |
|--------------------|-----------------------------|----------------------------------|
| Input Capture      | `pynput.keyboard.Listener`  | Hardware-level keystroke monitoring |
| Log Management     | `logging` + `os` modules    | Structured file handling          |
| Data Transmission  | `smtplib` + `email` package | Secure log delivery              |
| Data Encoding      | `base64` + `re`             | Payload obfuscation              |
| Time Management    | `datetime`                  | Precise event timestamping       |

---

## **🔧 Setup & Configuration Guide**

### **🖥️ Local Testing Setup**
1. Install Python 3.8+  
2. Configure local SMTP server: Run on Windows terminal, then run the main keylogger script.
   ```bash
   python -m aiosmtpd -n -l localhost:1025 --debug
   ```
3. Install dependencies:
   ```bash
   pip install pynput
   pip install aiosmtpd
   ```

### **✉️ Email Reporting Setup**
1. Edit SMTP credentials in the detection/yara_keyloggerdetect.py:
   ```python
   SMTP_SERVER = "localhost"  
   SMTP_PORT = 1025                 
   USE_TLS = False                    
   ```
2. Configure sender/receiver emails
3. Test email functionality before deployment
4. Run the program in src/keylogger_mail.py

---

## **⚠️ Enhanced Ethical Warning**

**THIS TOOL DEMONSTRATES:**
- System monitoring capabilities
- Covert data collection techniques
- Anti-forensic methods

**LEGAL REQUIREMENTS:**
1. **Written consent** from monitored users
2. **Corporate policy compliance** for work systems
3. **Data protection law** adherence (GDPR, CCPA, etc.)
4. **Never** deploy on unauthorized systems

**Recommended Use Cases:**

✅ Parental control systems (with consent)  
✅ Corporate security audits (authorized only)  
✅ Cybersecurity education  
✅ Penetration testing (with written permission)

---

## **🔍 Forensic Analysis Perspective**

**Detectable Artifacts:**
1. Running processes matching `python keylogger_mail.py`
2. Outbound SMTP connections
3. Log file creation/modification timestamps
4. Python interpreter hooks

**Anti-Forensic Measures (For Research):**
- **Fileless operation** (logs in memory only)
- **Alternate data exfiltration** (DNS tunneling)
- **Process injection** (DLL hijacking)
- **Rootkit techniques** (not implemented)

---

## **🚀 Roadmap & Future Development**

```mermaid
graph LR
A[Current Version] --> B[Add AES Encryption]
A --> C[Implement C2 Server]
A --> D[Add Screenshot Capture]
B --> E[Multi-Platform Support]
C --> F[Tor Hidden Service]
```

**Planned Features:**
1. **Data Encryption** (AES-256)
2. **Command & Control** (WebSocket)
3. **Evasion Techniques** (Process hollowing)
4. **Breadth Expansion** (Clipboard logging)

---

## **📚 Learning Resources**

1. **Python Documentation**
   - `pynput` library
   - `logging` module
   - `smtplib` examples

2. **Cybersecurity References**
   - MITRE ATT&CK Framework
  ```mermaid
  graph LR
A[Keylogger] --> B[T1056.001: Input Capture]
A --> C[T1071: Application Layer Protocol]
A --> D[T1041: Exfiltration Over C2 Channel]
```
   - 
   - OWASP Top 10
   - NIST SP 800-115

3. **Legal Guidelines**
   - Computer Fraud and Abuse Act
   - General Data Protection Regulation
   - Local cyber laws

---

# **🎯 Final Notes**  
This project serves as **an educational tool** to understand:  
- System monitoring principles  
- Defensive programming techniques  
- Ethical hacking methodologies  

**Remember:**  
🔹 With great power comes great responsibility  
🔹 Always obtain proper authorization  
🔹 Use knowledge to improve security, not compromise it  

**Happy (Ethical) Hacking!** 🔐💻
