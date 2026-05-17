import requests
import argparse

# Argument parser
parser = argparse.ArgumentParser(description="Simple Subdomain Finder")

parser.add_argument("-d", "--domain", required=True,
                    help="Target domain")

parser.add_argument("-w", "--wordlist", required=True,
                    help="Path to wordlist")

args = parser.parse_args()

domain = args.domain
wordlist_path = args.wordlist

# Read wordlist
with open(wordlist_path, "r") as file:
    subdomains = file.read().splitlines()

# Scan subdomains
for sub in subdomains:
    url = f"http://{sub}.{domain}"

    try:
        response = requests.get(url, timeout=3)

        print(f"[+] Found: {url} ({response.status_code})")

    except requests.ConnectionError:
        pass

    except requests.RequestException:
        pass