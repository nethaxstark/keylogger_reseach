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
```
## Network Detection

**Wire Shark**
```
# SMTP Exfiltration
smtp && frame contains "MAIL FROM" && (frame contains "keylog" || frame contains "keystroke")

# HTTP Exfiltration
http.request.method == "POST" && (http.file_data contains "key=" || http.file_data contains "log=")

# DNS Exfiltration
dns.qry.name matches /[a-z0-9]{16}\.exfil\.com/
```
## Detection Tools

**Endpoint**
```
Tool	Usage	Command Example
YARA	File scanning	yara rules.yar suspicious.exe
Sysmon	Process monitoring	Get-WinEvent -Path sysmon.evtx
OSQuery	Live system queries	SELECT * FROM processes WHERE cmdline LIKE '%pynput%'
```
**Network**
```
Tool	Usage	Command Example
Zeek	Protocol analysis	zeek -r traffic.pcap
Suricata	IDS/IPS	suricata -c suricata.yaml -r traffic.pcap
Wireshark	Manual inspection	tcp.port == 587 && smtp
```
**Memory**
```
Tool	Usage	Command Example
Volatility	Memory forensics	vol.py -f memory.dump pslist
Rekall	Memory analysis	rekall -f memory.img pslist
Redline	IOC hunting	Manual analysis via GUI
```
