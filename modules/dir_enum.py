"""
Basic Directory Enumerator
"""

import requests

COMMON = [
    "admin",
    "login",
    "robots.txt",
    "dashboard",
    "backup",
]


def scan(url):

    found = []

    for path in COMMON:

        target = url.rstrip("/") + "/" + path

        try:

            response = requests.get(
                target,
                timeout=5
            )

            if response.status_code < 400:

                found.append(
                    {
                        "path": target,
                        "status": response.status_code
                    }
                )

        except Exception:
            pass

    return found