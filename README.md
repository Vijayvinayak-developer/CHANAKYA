# CHANAKYA

CHANAKYA is a beginner-friendly modular reconnaissance framework built in Python for learning networking, OSINT, and cybersecurity automation.

Inspired by ancient strategist :contentReference[oaicite:0]{index=0}.

---

# Features

- Ping Scanner
- WHOIS Lookup
- Nmap Integration
- Banner Grabbing
- Directory Finder
- Subdomain Finder

---

# Modules

| Module | Description |
|---|---|
| Ping | Checks if host is alive |
| Whois | Retrieves domain information |
| Nmap | Service and version detection |
| Banner Grabber | Captures service banners |
| Directory Finder | Finds hidden directories |
| Subdomain Finder | Discovers subdomains |

---

# Project Structure

```text
CHANAKYA/
│
├── banner.py
├── dir.py
├── dom.py
├── chanakya.py
├── installer.sh
├── run.sh
├── wordlists/
└── README.md
```

---

# Installation

## Linux / Kali Linux

Run installer:

```bash
chmod +x installer.sh
./installer.sh
```

---

# Running CHANAKYA

```bash
chmod +x run.sh
./run.sh
```

Or directly:

```bash
python3 chanakya.py
```

---


# Example Usage

```text
Enter ip of target: 8.8.8.8
Enter target url: example.com
Enter wordlist path for subdomain: subdomains.txt
Enter wordlist path for subdir: dirs.txt
```

---

# Example Output

```text
[+] Running Ping Scan...
[+] Running Whois...
[+] Running Nmap...
[+] Running Banner Grabber...
[+] Running Directory Finder...
[+] Running Subdomain Finder...
[+] Recon Completed
```

---

# Future Improvements

- Threading
- Async scanning
- GUI Dashboard
- Report generation
- Colored terminal output
- Plugin system
- AI-powered recon summaries
- Screenshot module
- DNS enumeration
- SSL analysis

---

# Educational Purpose

This project is intended for:
- learning Python
- understanding networking
- studying reconnaissance workflows
- cybersecurity education

Only scan systems you own or have permission to test.

---

# Inspiration

Inspired by tools such as:
- :contentReference[oaicite:1]{index=1}
- :contentReference[oaicite:2]{index=2}
- :contentReference[oaicite:3]{index=3}

---

# Author

Vijayvinayak
