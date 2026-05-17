import subprocess as spro
from pyfiglet import figlet_format

pbanner = figlet_format("CHANAKYA")

print(pbanner)
print("                                     by vijayvinayak")

banner = """
====================================
        CHANAKYA RECON TOOL
====================================

1. Ping
2. Whois
3. Nmap
4. Banner Grab
5. Directory Finder
6. Subdomain Finder
"""

print(banner)

target_ip = input("Enter ip of target: ")
target_url = input("Enter target url: ") 
wordlist_subdomain = input("Enter wordlist path for subdomain: ")
wordlist_dir = input("Enter wordlist path for subdir: ")



def Ping():
    spro.run([
        "ping",
        "-c",
        "4",
        target_ip
    ])

def Who():
    spro.run([
        "whois",
        target_url 
    ])

def Nmap():
    spro.run([
        "nmap",
        "-sC",
        "-sV",
        "-vvv",
        target_ip
    ])  

def Ban():
    spro.run([
        "python3",
        "banner.py",
        "-t",
        target_ip,
        "-p",
        "21"

    ])

def Dirfind():
    spro.run([
        "python3",
        "dir.py",
        "-u",
        target_url,
        "-w",
        wordlist_dir
        
    ])

def Domfind():
    spro.run([
       "python3",
        "dom.py",
        "-d",
        target_url,
        "-w",
        wordlist_subdomain
    ])


print("\n[+] Running Ping Scan...\n")
Ping()

print("\n[+] Running Whois...\n")
Who()

print("\n[+] Running Nmap...\n")
Nmap()

print("\n[+] Running Banner Grabber...\n")
Ban()

print("\n[+] Running Directory Finder...\n")
Dirfind()

print("\n[+] Running Subdomain Finder...\n")
Domfind()

print("\n[+] Recon Completed")
