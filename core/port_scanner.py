import socket

def run_port_scan(target, mode="fast"):
    print("[INFO] PORT SCAN")

    ports = [21, 22, 80, 443, 8080] if mode == "fast" else range(1, 1025)

    services = {
        80: "HTTP",
        443: "HTTPS",
        21: "FTP",
        22: "SSH",
        8080: "HTTP-ALT"
    }

    open_ports = []

    for port in ports:
        s = socket.socket()
        s.settimeout(1)

        try:
            s.connect((target, port))
            service = services.get(port, "Unknown")
            print(f"[OPEN] {port} → {service}")
            open_ports.append(port)
            s.close()
        except:
            pass

    return open_ports