# Keylogger Detection Techniques

## 🔍 Behavioral Indicators
1. **Process Monitoring**
   - Unusual Python processes with:
     ```bash
     ps aux | grep -i "pynput\|keyboard"
     ```
2. **File System Changes**
   - Monitor for `keylogs.txt` creation:
     ```powershell
     Get-WinEvent -FilterHashtable @{Path='Security'; Id=4657} | Where-Object {$_.Message -like "*keylogs.txt*"}
     ```

## 🛡️ Detection Tools
### YARA Rule
```yara
rule Python_Keylogger {
    meta:
        description = "Detects Python keyloggers"
    strings:
        $pynput = "pynput.keyboard"
        $hook = "keyboard.Listener"
    condition:
        any of them
}
