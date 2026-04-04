def analyze_risk(ports):
    print("\n[INFO] RISK ANALYSIS")

    if not ports:
        print("[INFO] No open ports found")
        return

    for port in ports:
        if port in [21, 23]:
            print(f"[HIGH] Port {port}")
            if port == 21:
                print("      ↳ FTP (Insecure)")
        elif port in [80, 443]:
            print(f"[MEDIUM] Port {port}")
        else:
            print(f"[LOW] Port {port}")