"""
Simple Subdomain Enumerator
"""

import socket

COMMON = [
    "www",
    "mail",
    "ftp",
    "api",
    "dev",
    "test",
    "admin",
    "blog",
]


def scan(domain):

    found = []

    for sub in COMMON:

        host = f"{sub}.{domain}"

        try:

            ip = socket.gethostbyname(host)

            found.append(
                {
                    "host": host,
                    "ip": ip
                }
            )

        except:

            pass

    return found