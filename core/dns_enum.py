import socket

def run_dns_enum(target):
    print("[INFO] DNS ENUMERATION")

    try:
        ip = socket.gethostbyname(target)
        print(f"[A] {ip}")
    except:
        print("[ERROR] A record failed")

    try:
        rev = socket.gethostbyaddr(ip)
        print(f"[PTR] {rev[0]}")
    except:
        print("[WARNING] No reverse DNS")