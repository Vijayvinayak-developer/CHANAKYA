import requests
import argparse

# Argument parser
parser = argparse.ArgumentParser(description="Simple Directory Finder")

parser.add_argument("-u", "--url", required=True,
                    help="Target URL")

parser.add_argument("-w", "--wordlist", required=True,
                    help="Path to wordlist")

args = parser.parse_args()

target = args.url
wordlist_path = args.wordlist

# Read wordlist
with open(wordlist_path, "r") as file:
    words = file.read().splitlines()

# Scan directories
for word in words:
    url = f"{target}/{word}"

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            print(f"[+] Found: {url}")

        elif response.status_code == 403:
            print(f"[!] Forbidden: {url}")

        else:
            print(f"[-] {response.status_code}: {url}")

    except requests.exceptions.RequestException:
        print(f"[X] Error: {url}")