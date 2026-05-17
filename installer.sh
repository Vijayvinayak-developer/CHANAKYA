#!/bin/bash

echo "[+] Updating packages..."
sudo apt update && sudo apt upgrade -y

echo "[+] Installing Python..."
sudo apt install python3 python3-pip -y

echo "[+] Installing Recon Tools..."
sudo apt install nmap whois dnsutils -y

echo "[+] Installing Python Libraries..."
pip3 install requests pyfiglet rich dnspython python-whois

echo "[+] Installation Complete!"
echo "[+] You can now run your CHANAKYA recon tool" 
