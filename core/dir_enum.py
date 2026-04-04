import requests

def run_dir_enum(target, mode="fast"):
    print("[INFO] DIRECTORY ENUMERATION")

    found = []

    # 🔹 protocol auto handle
    base_url = f"http://{target}"

    # 🔹 wordlist load
    with open("data/dirs.txt") as f:
        dirs = f.read().splitlines()

    for d in dirs:
        url = f"{base_url}/{d}"

        try:
            r = requests.get(url, timeout=2)

            # 🔥 better filtering
            if r.status_code == 200:
                print(f"[FOUND] /{d} → 200 (OK)")
                found.append(url)

            elif r.status_code == 403:
                print(f"[FORBIDDEN] /{d} → 403 (Protected)")
                found.append(url)

            elif r.status_code == 301 or r.status_code == 302:
                print(f"[REDIRECT] /{d} → {r.status_code}")

        except requests.exceptions.RequestException:
            pass

    return found