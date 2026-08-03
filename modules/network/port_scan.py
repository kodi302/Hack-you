"""
Hack-You Professional Port Scanner
Version : 3.0
"""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-ALT",
}


def scan_port(target, port, timeout=0.5):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:

        if sock.connect_ex((target, port)) == 0:

            return {
                "port": port,
                "service": COMMON_PORTS.get(port, "Unknown"),
                "state": "open"
            }

    except Exception:
        pass

    finally:
        sock.close()

    return None


def scan(target, ports=None):

    results = []

    if ports is None:
        ports = list(COMMON_PORTS.keys())
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            
            futures = [
            executor.submit(scan_port, target, port)
            for port in ports
            ]

        for future in as_completed(futures):

            data = future.result()

            if data:
                results.append(data)

    results.sort(key=lambda x: x["port"])

    return {
        "target": target,
        "ports": results
    }