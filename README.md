## 🔐 Keylogger Tool - Project Overview

(Educational Purposes Only!)
🌐 Project Overview

This Python-based Keylogger Tool captures and logs keyboard inputs, with advanced features like log rotation and email reporting.
⚙️ Core Features

✔ Keystroke Logging → Records all keyboard inputs
✔ Log Rotation → Prevents oversized log files
✔ Email Reporting → Sends logs via SMTP
✔ Base64 Decoding → Handles encoded email attachments
✔ User-Friendly → Simple start/stop with ESC key
📜 Code Structure
python

📂 keylogger.py
├── 📜 IMPORTS
│   ├── pynput.keyboard → Keypress detection
│   ├── logging → Log file management  
│   ├── smtplib → Email sending  
│   ├── base64 → Email attachment decoding  
│   └── datetime → Timestamp generation  
│
├── ⚙️ CONFIGURATION  
│   ├── LOG_FILE = "keylogs.txt"  
│   ├── MAX_SIZE = 1MB  
│   └── Email settings (SMTP server, ports, etc.)  
│
├── 🔧 FUNCTIONS  
│   ├── setup_logging() → Configures log file  
│   ├── on_press() → Handles keypress events  
│   ├── check_log_size() → Manages log rotation  
│   ├── decode_base64_logs() → Decodes email attachments  
│   └── send_logs_via_email() → Sends logs via SMTP  
│
└── 🚀 MAIN EXECUTION  
    ├── Starts keylogger  
    ├── Listens for ESC key to stop  
    └── Optionally sends logs via email  

🔍 Technical Deep Dive
1️⃣ Keystroke Logging (on_press())

    Uses pynput.keyboard to detect keypresses

    Logs normal keys (A-Z, 0-9) and special keys (Enter, Shift, etc.)

    Example log format:
    text

    2024-05-20 12:34:56: Key pressed: H  
    2024-05-20 12:34:56: Key pressed: i  
    2024-05-20 12:34:56: [ENTER]  

2️⃣ Log Rotation (check_log_size())

    Automatically renames log file if it exceeds 1MB

    Backup format: keylog_YYYYMMDD_HHMMSS.txt

3️⃣ Email Reporting (send_logs_via_email())

    Uses SMTP to send logs to a predefined email

    Attaches log file as .txt

    Supports Base64 decoding for email preview

4️⃣ Base64 Decoding (decode_base64_logs())

    Extracts and decodes Base64-encoded email attachments

    Handles padding errors automatically

    Supports both text & binary data

🚀 How It Works

    Run the script → Starts logging keystrokes

    Press ESC → Stops the keylogger

    Choose y/n → Optionally email logs

    Check keylogs.txt → All keystrokes saved

⚠️ Legal & Ethical Warning

❗ This tool is for EDUCATIONAL USE ONLY!
❗ Unauthorized monitoring is ILLEGAL.
❗ Only use on systems you OWN or have EXPLICIT PERMISSION to test.
🔧 How to Run

1️⃣ Install dependencies:
bash

pip install pynput

2️⃣ Execute:
bash

python keylogger.py

3️⃣ Press ESC to stop.
🎯 Conclusion

This tool demonstrates keylogging, file management, and email automation in Python. Use responsibly!

🔹 For cybersecurity education only!
🔹 Never deploy without consent.

🚨 Stay ethical, stay legal! 🚨
