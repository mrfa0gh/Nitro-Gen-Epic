import requests
import random

# قراءة البروكسيات من الملف وتحويلها للصيغة الصحيحة
def format_proxy(line):
    parts = line.strip().split(":")
    if len(parts) == 4:
        ip, port, user, pwd = parts
        return f"http://{user}:{pwd}@{ip}:{port}"
    elif len(parts) == 2:
        return f"http://{parts[0]}:{parts[1]}"
    else:
        return None

with open("proxy.txt", "r") as f:
    proxies_raw = [format_proxy(line) for line in f if format_proxy(line)]

# اختيار بروكسي عشوائي
proxy_url = random.choice(proxies_raw)

proxies = {
    "http": proxy_url,
    "https": proxy_url
}

url = "https://discord.com/api/v9/entitlements/gift-codes/NXjjBFjZDNT6rWzDEV8jsVJd"
headers = {
    "Authorization": "Again_token_here"
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://discord.com/billing/promotions/NXjjBFjZDNT6rWzDEV8jsVJd",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "X-Discord-Locale": "en-US",
    "X-Discord-Timezone": "Africa/Cairo",
    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImNsaWVudF9sYXVuY2hfaWQiOiI1OWE5ZTE0Zi04OGI5LTQ5ZmYtYjFjNC00MDY4MzI2OTNlODMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo0MDI4NjksImNsaWVudF9hcHBfc3RhdGUiOiJmb2N1c2VkIn0="
}

params = {
    "country_code": "EG",
    "with_application": "false",
    "with_subscription_plan": "true"
}
#proxies=proxies,
try:
    response = requests.get(url, headers=headers, params=params,      timeout=15)
    print("Status Code:", response.status_code)
    print("Response JSON:")
    print(response.json())
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
