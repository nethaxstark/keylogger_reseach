rule Python_Keylogger {
    meta:
        author = "Ajay Kumar"
        date = "2025-06-19"
        description = "Detects Python keyloggers using pynput"
        reference = "https://github.com/nethaxstark"

    strings:
        // Code patterns
        $pynput_import = "from pynput import keyboard" ascii wide
        $listener_start = "keyboard.Listener(" ascii wide
        $on_press = "def on_press(" ascii wide
        
        // Behavioral indicators
        $logging_call = "logging.info(f\"Key pressed:" ascii wide
        $smtp_exfil = "smtplib.SMTP(" ascii wide

    condition:
        // Match if 2+ code patterns are found in small files
        (filesize < 500KB) and 
        (2 of ($pynput_import, $listener_start, $on_press)) or
        (1 of ($logging_call, $smtp_exfil))
}
