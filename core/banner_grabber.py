"""
Hack-You Banner Grabber
"""

import socket


def grab_banner(target, port, timeout=2):

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        sock.connect((target, port))

        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        except Exception:
            pass

        banner = sock.recv(1024).decode(
            errors="ignore"
        ).strip()

        sock.close()

        if banner:
            return banner

        return "No Banner"

    except Exception:

        return "Unknown"