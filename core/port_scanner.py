"""
Hack-You Professional Port Scanner
Version : 2.0
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
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-ALT",
}


def scan_port(target, port, timeout=1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:

        if sock.connect_ex((target, port)) == 0:

            banner = ""

            try:

                banner = sock.recv(1024).decode(
                    errors="ignore"
                ).strip()

            except Exception:
                pass

            return {
                "port": port,
                "service": COMMON_PORTS.get(
                    port,
                    "Unknown"
                ),
                "banner": banner,
                "state": "open",
            }

    except Exception:
        pass

    finally:
        sock.close()

    return None


def run_port_scan(
    target,
    mode="fast",
    threads=100
):

    if mode == "fast":

        ports = list(COMMON_PORTS.keys())

    else:

        ports = range(1, 1025)

    results = []

    with Progress() as progress:

        task = progress.add_task(
            "[cyan]Scanning Ports...",
            total=len(ports)
        )

        with ThreadPoolExecutor(
            max_workers=threads
        ) as executor:

            futures = [
                executor.submit(
                    scan_port,
                    target,
                    port
                )
                for port in ports
            ]

            for future in as_completed(futures):

                data = future.result()

                if data:
                    results.append(data)

                progress.update(
                    task,
                    advance=1
                )

    return results