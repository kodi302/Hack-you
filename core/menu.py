from rich.console import Console
from rich.panel import Panel
import questionary

from core.banner import show
from core.port_scanner import run_port_scan
from core.dns_enum import run_dns_enum
from core.subdomain_enum import run_subdomain_enum
from core.dir_enum import run_dir_enum
from core.whois import lookup
from core.reporter import generate_report
from core.risk_engine import analyze_risk

from core.scanner_menu import port_menu
from core.shell import start_shell
from core.logger import info

console = Console()


def about():

    console.print(
        Panel.fit(
            """
Hack-You v2.1

Professional Cyber Security Toolkit

Developer : Praveen Rawat

GitHub :
https://github.com/kodi302/Hack-you
"""
        )
    )

    input("\nPress Enter...")


def full_scan():

    target = questionary.text(
        "Enter Target"
    ).ask()

    info(f"Full Scan Started : {target}")

    dns = run_dns_enum(target)

    subs = run_subdomain_enum(target)

    ports = run_port_scan(target)

    dirs = run_dir_enum(target)

    analyze_risk(
        [p["port"] for p in ports]
    )

    generate_report(
        target,
        dns,
        subs,
        ports,
        dirs
    )

    info(f"Full Scan Completed : {target}")

    input("\nPress Enter...")


def start():

    while True:

        console.clear()

        show()

        option = questionary.select(

            "Choose Module",

            choices=[

                "Port Scanner",

                "DNS Enumeration",

                "Subdomain Enumeration",

                "Directory Scanner",

                "WHOIS Lookup",

                "Full Scan",

                "Interactive Shell",

                "Reports",

                "Settings",

                "About",

                "Exit"

            ]

        ).ask()

        if option == "Port Scanner":

            port_menu()

        elif option == "DNS Enumeration":

            target = questionary.text(
                "Enter Domain"
            ).ask()

            console.print(
                run_dns_enum(target)
            )

            input("\nPress Enter...")

        elif option == "Subdomain Enumeration":

            target = questionary.text(
                "Enter Domain"
            ).ask()

            console.print(
                run_subdomain_enum(target)
            )

            input("\nPress Enter...")

        elif option == "Directory Scanner":

            target = questionary.text(
                "Enter URL"
            ).ask()

            console.print(
                run_dir_enum(target)
            )

            input("\nPress Enter...")

        elif option == "WHOIS Lookup":

            target = questionary.text(
                "Enter Domain"
            ).ask()

            console.print(
                lookup(target)
            )

            input("\nPress Enter...")

        elif option == "Full Scan":

            full_scan()

        elif option == "Interactive Shell":

            start_shell()

        elif option == "Reports":

            console.print(
                "\nReports Module Coming Soon..."
            )

            input()

        elif option == "Settings":

            console.print(
                "\nSettings Module Coming Soon..."
            )

            input()

        elif option == "About":

            about()

        elif option == "Exit":

            console.print(
                "\nGood Bye!"
            )

            break