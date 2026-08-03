from rich.console import Console
from rich.panel import Panel

from core.port_scanner import run_port_scan
from core.dns_enum import run_dns_enum
from core.subdomain_enum import run_subdomain_enum
from core.dir_enum import run_dir_enum
from core.whois import lookup
from core.reporter import generate_report
from core.risk_engine import analyze_risk

console = Console()


def help_menu():
    console.print(Panel.fit("""
Commands

help

scan port <target>

scan dns <domain>

scan subdomain <domain>

scan dir <url>

whois <domain>

fullscan <target>

clear

exit
"""))


def start_shell():

    console.print("\n[green]Hack-You Interactive Shell[/green]")

    while True:

        cmd = input("\nhackyou > ").strip()

        if cmd == "help":

            help_menu()

        elif cmd.startswith("scan port"):

            target = cmd.replace("scan port", "").strip()

            ports = run_port_scan(target)

            console.print(ports)

            analyze_risk([p["port"] for p in ports])

        elif cmd.startswith("scan dns"):

            target = cmd.replace("scan dns", "").strip()

            console.print(run_dns_enum(target))

        elif cmd.startswith("scan subdomain"):

            target = cmd.replace("scan subdomain", "").strip()

            console.print(run_subdomain_enum(target))

        elif cmd.startswith("scan dir"):

            target = cmd.replace("scan dir", "").strip()

            console.print(run_dir_enum(target))

        elif cmd.startswith("whois"):

            target = cmd.replace("whois", "").strip()

            console.print(lookup(target))

        elif cmd.startswith("fullscan"):

            target = cmd.replace("fullscan", "").strip()

            dns = run_dns_enum(target)
            subs = run_subdomain_enum(target)
            ports = run_port_scan(target)
            dirs = run_dir_enum(target)

            analyze_risk([p["port"] for p in ports])

            generate_report(
                target,
                dns,
                subs,
                ports,
                dirs
            )

            console.print("\n[green]Scan Finished[/green]")

        elif cmd == "clear":

            console.clear()

        elif cmd == "exit":

            break

        else:

            console.print("[red]Unknown Command[/red]")