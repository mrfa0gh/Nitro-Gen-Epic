import requests, random, string, threading, os
from concurrent.futures import ThreadPoolExecutor

valid = 0
invalid = 0
lock = threading.Lock()

with open("proxy.txt", "r") as f:
    proxies_list = [line.strip() for line in f if line.strip()]
proxy_count = len(proxies_list)
print('''

███    ██ ██ ████████ ██████   ██████       ██████  ███████ ███    ██ 
████   ██ ██    ██    ██   ██ ██    ██     ██       ██      ████   ██ 
██ ██  ██ ██    ██    ██████  ██    ██     ██   ███ █████   ██ ██  ██ 
██  ██ ██ ██    ██    ██   ██ ██    ██     ██    ██ ██      ██  ██ ██ 
██   ████ ██    ██    ██   ██  ██████       ██████  ███████ ██   ████ 
                                                                      
                                                                      

██████  ██    ██      ██████  ██   ██  █████  ██      ██     ██  █████  ███████ ██   ██ 
██   ██  ██  ██      ██       ██   ██ ██   ██ ██      ██     ██ ██   ██ ██      ██   ██ 
██████    ████       ██   ███ ███████ ███████ ██      ██  █  ██ ███████ ███████ ███████ 
██   ██    ██        ██    ██ ██   ██ ██   ██ ██      ██ ███ ██ ██   ██      ██ ██   ██ 
██████     ██         ██████  ██   ██ ██   ██ ███████  ███ ███  ██   ██ ███████ ██   ██ 
                                                                                        
                                @Mrfa0gh
                                ''')

def generate_code():
    return 'J' + ''.join(random.choices(string.ascii_letters + string.digits, k=23))

def update_title():
    os.system(f"title Nitro By Ghalwash : Valid : {valid}      Invalid : {invalid}           proxy: {proxy_count}   @mrfa0gh")

def format_proxy(line):
    parts = line.split(":")
    if len(parts) == 4:
        return f"http://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}"
    elif len(parts) == 2:
        return f"http://{parts[0]}:{parts[1]}"
    return None

def check_code():
    global valid, invalid
    while True:
        code = generate_code()
        url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?country_code=EG&with_application=false&with_subscription_plan=true"
        proxy_raw = random.choice(proxies_list)
        proxy_url = format_proxy(proxy_raw)
        proxies = {"http": proxy_url, "https": proxy_url}
        headers = {
            "Authorization": "Your_Dumb_token_Here",
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
        

        try:
            #proxies=proxies,
            response = requests.get(url, headers=headers,    timeout=10)
            if "You got one month of Nitro!" in response.text:
                with lock:
                    valid += 1
                    with open("nitro.txt", "a") as f:
                        f.write(f"https://discord.gift/{code}\n")
            else:
                with lock:
                    invalid += 1
        except:
            with lock:
                invalid += 1
        update_title()

# حدد عدد الـ Threads
max_threads = 50

with ThreadPoolExecutor(max_workers=max_threads) as executor:
    for _ in range(max_threads):
        executor.submit(check_code)
