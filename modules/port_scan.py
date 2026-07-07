"""
Hack-You Professional Port Scanner
"""

import socket

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


def scan(target: str, timeout: float = 1.0):
    """
    Scan common TCP ports on a target host.
    """

    results = {
        "target": target,
        "ports": []
    }

    for port, service in COMMON_PORTS.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        try:
            if sock.connect_ex((target, port)) == 0:
                results["ports"].append(
                    {
                        "port": port,
                        "service": service,
                        "state": "open"
                    }
                )
        except Exception:
            pass
        finally:
            sock.close()

    return results