import requests

def run_subdomain_enum(target, mode="fast"):
    print("[INFO] SUBDOMAIN ENUMERATION")

    found = []

    # 🔹 wordlist load
    with open("data/subdomains.txt") as f:
        subs = f.read().splitlines()

    for sub in subs:
        url_http = f"http://{sub}.{target}"
        url_https = f"https://{sub}.{target}"

        try:
            # 🔥 pehle HTTPS try
            r = requests.get(url_https, timeout=2)
            print(f"[FOUND] {url_https} → {r.status_code}")
            found.append(url_https)

        except:
            try:
                # fallback HTTP
                r = requests.get(url_http, timeout=2)
                if r.status_code < 400:
                    print(f"[FOUND] {url_http} → {r.status_code}")
                    found.append(url_http)
            except:
                pass

    return found