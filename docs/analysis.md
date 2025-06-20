# Localhost Network Analysis with Wireshark & Npcap

## Table of Contents
1. [Npcap Setup]()
2. [Capturing Localhost Traffic]()
3. [Keylogger Traffic Patterns]()
4. [SMTP Analysis]()
5. [HTTP Exfiltration]()
6. [Advanced Filters]()
7. [Forensic Artifacts]()

---

## 1. Npcap Setup

### Installation
```powershell
# Download from https://npcap.com/
# Install with these options:
☑ Install Npcap in WinPcap API-compatible Mode
☑ Support loopback traffic ("Npcap Loopback Adapter")
```
# Network Forensics: Keylogger Traffic Analysis Guide

## 1. Npcap Verification
```powershell
> npcap-status
# Expected output:
# "Loopback traffic capture: Supported"

2. Localhost Traffic Capture
Basic Configuration

    Select "Npcap Loopback Adapter" in Wireshark

    Apply base filter:

text

tcp.port == 1025 || tcp.port == 587 || tcp.port == 25

Essential Filters
wireshark
```

# General loopback traffic
tcp and (ip.src == 127.0.0.1 or ip.dst == 127.0.0.1)

# Keylogger indicators
tcp contains "keylog" || tcp contains "keystroke"

3. Keylogger Traffic Patterns
SMTP Exfiltration Pattern
text

Frame 1: TCP SYN (Src: 127.0.0.1:49234 → Dst: 127.0.0.1:1025)
Frame 2: SMTP "EHLO localhost"
Frame 3: "MAIL FROM:<sender@localhost>"
Frame 4: "RCPT TO:<receiver@localhost>"
Frame 5: DATA with base64-encoded payload

HTTP POST Exfiltration
http

POST /upload.php HTTP/1.1
Host: localhost
Content-Type: multipart/form-data

------WebKitFormBoundary
Content-Disposition: form-data; name="logfile"; filename="keystrokes.txt"
Content-Type: text/plain

[Actual keylog data...]

4. SMTP Analysis Techniques
Cleartext SMTP (Port 1025)
wireshark

smtp and tcp.port == 1025

Analysis Method: Right-click → Follow → TCP Stream → Show as "ASCII"
Encrypted SMTP (Port 587)
wireshark
```
```
# Pre-encryption
smtp.req.command == "STARTTLS"

# Post-encryption (requires server key)
tls and tcp.port == 587

5. HTTP Exfiltration Analysis
Detection Filters
wireshark

# Basic detection
http.request.method == "POST" && http.file_data

# Keylogger-specific
http contains "keylog" || http contains "keystroke"

File Extraction Process

    Apply filter: http.content_type contains "multipart"

    Right-click → Export Packet Bytes → Save as "upload.bin"

    Extract contents:

bash

binwalk -e upload.bin

6. Advanced Analysis Techniques
Timing Analysis
wireshark

# Frequent small packets
frame.time_delta < 0.1 && tcp.len < 50

# Traffic bursts
tcp.analysis.ack_rtt > 0.5 && tcp.len > 0

Payload Patterns
wireshark

# Base64 exfiltration
tcp.payload matches "[A-Za-z0-9+/=]{20,}"

# JSON-formatted data
tcp.payload matches "\"keys\":\[.*\]"

7. Forensic Artifacts
Wireshark Statistics

    Conversations: Statistics → Conversations → TCP

    Flow Graph: Statistics → Flow Graph

    HTTP Objects: File → Export Objects → HTTP
