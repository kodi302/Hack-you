"""
Hack-You Professional Subdomain Enumerator
Version : 2.0
"""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress

COMMON_SUBDOMAINS = [
    "www",
    "mail",
    "ftp",
    "api",
    "dev",
    "test",
    "stage",
    "admin",
    "beta",
    "blog",
    "shop",
    "cdn",
    "ns1",
    "ns2",
    "smtp",
    "webmail",
    "cpanel",
]


def check_subdomain(domain, sub):

    host = f"{sub}.{domain}"

    try:

        ip = socket.gethostbyname(host)

        return {
            "subdomain": host,
            "ip": ip,
        }

    except Exception:

        return None


def run_subdomain_enum(
    domain,
    mode="fast",
    threads=50
):

    if mode == "fast":
        wordlist = COMMON_SUBDOMAINS
    else:
        wordlist = COMMON_SUBDOMAINS

    results = []

    with Progress() as progress:

        task = progress.add_task(
            "[cyan]Enumerating Subdomains...",
            total=len(wordlist)
        )

        with ThreadPoolExecutor(
            max_workers=threads
        ) as executor:

            futures = [
                executor.submit(
                    check_subdomain,
                    domain,
                    sub
                )
                for sub in wordlist
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