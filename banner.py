import socket
import argparse

# Argument parser
parser = argparse.ArgumentParser(description="Simple Banner Grabber")

parser.add_argument("-t", "--target", required=True,
                    help="Target IP or domain")

parser.add_argument("-p", "--port", required=True, type=int,
                    help="Target port")

args = parser.parse_args()

target = args.target
port = args.port

try:
    # Create socket
    s = socket.socket()
    s.settimeout(3)

    # Connect
    s.connect((target, port))

    # Receive banner
    banner = s.recv(1024).decode(errors="ignore")

    print(f"[+] Banner from {target}:{port}")
    print(banner)

    s.close()

except Exception as e:
    print(f"[-] Error: {e}")