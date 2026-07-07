"""
Hack-You Professional Directory Enumerator
Version : 2.0
"""

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress

COMMON_PATHS = [
    "admin",
    "login",
    "dashboard",
    "robots.txt",
    "sitemap.xml",
    ".git",
    ".env",
    "backup",
    "config",
    "uploads",
    "images",
    "css",
    "js",
    "api",
    "wp-admin",
    "phpmyadmin",
    "server-status",
    "test",
    "dev",
    "panel"
]


def scan_path(base_url, path, timeout=5):

    url = base_url.rstrip("/") + "/" + path

    try:

        r = requests.get(
            url,
            timeout=timeout,
            allow_redirects=True,
            headers={
                "User-Agent": "Hack-You Scanner"
            }
        )

        if r.status_code < 400:

            return {
                "url": url,
                "status": r.status_code,
                "length": len(r.text),
                "server": r.headers.get("Server", ""),
                "title": (
                    r.text.split("<title>")[1].split("</title>")[0]
                    if "<title>" in r.text.lower()
                    else ""
                )
            }

    except Exception:
        pass

    return None


def run_dir_enum(
    target,
    mode="fast",
    threads=50
):

    if not target.startswith("http"):
        target = "http://" + target

    results = []

    with Progress() as progress:

        task = progress.add_task(
            "[cyan]Directory Scan...",
            total=len(COMMON_PATHS)
        )

        with ThreadPoolExecutor(
            max_workers=threads
        ) as executor:

            futures = [
                executor.submit(
                    scan_path,
                    target,
                    path
                )
                for path in COMMON_PATHS
            ]

            for future in as_completed(futures):

                result = future.result()

                if result:
                    results.append(result)

                progress.update(
                    task,
                    advance=1
                )

    return results