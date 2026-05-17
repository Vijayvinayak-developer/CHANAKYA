#!/bin/bash

echo "[+] Updating packages..."
sudo apt update -y

echo "[+] Installing Python..."
sudo apt install python3 python3-pip -y

echo "[+] Installing Recon Tools..."
sudo apt install nmap whois -y

echo "[+] Installing Python Libraries..."
pip3 install requests pyfiglet

echo "[+] Installation Complete!"
echo "[+] CHANAKYA is ready to use"
