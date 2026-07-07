"""
Hack-You v2.0
Professional Main Entry
"""

from rich.console import Console
from rich.panel import Panel
from rich import print

from core.logger import info, error
from core.database import db

from core.dns_enum import run_dns_enum
from core.subdomain_enum import run_subdomain_enum
from core.port_scanner import run_port_scan
from core.dir_enum import run_dir_enum
from core.risk_engine import analyze_risk
from core.reporter import generate_report

console = Console()


def banner():

    console.print(
        Panel.fit(
            "[bold cyan]Hack-You v2.0[/bold cyan]\n"
            "Professional Reconnaissance Framework",
            border_style="green"
        )
    )


def get_target():

    while True:

        target = input("\nEnter Target (IP/Domain): ").strip()

        if target:
            return target

        print("[red]Target cannot be empty![/red]")


def main():

    banner()

    target = get_target()

    info(f"Target : {target}")

    try:

        console.print("\n[cyan]Running DNS Enumeration...[/cyan]")
        dns_data = run_dns_enum(target)

        console.print("[cyan]Running Subdomain Enumeration...[/cyan]")
        subs = run_subdomain_enum(target, "fast")

        console.print("[cyan]Running Port Scan...[/cyan]")
        open_ports = run_port_scan(target, "fast")

        console.print("[cyan]Running Directory Scan...[/cyan]")
        dirs = run_dir_enum(target, "fast")

        console.print("[cyan]Analyzing Risk...[/cyan]")
        analyze_risk(open_ports)

        console.print("[cyan]Generating Report...[/cyan]")
        generate_report(
            target,
            dns_data,
            subs,
            open_ports,
            dirs
        )

        db.add_scan(
            "Full Scan",
            target,
            "Completed"
        )

        console.print(
            "\n[bold green]✓ Scan Completed Successfully[/bold green]"
        )

    except KeyboardInterrupt:

        console.print("\n[yellow]Scan Cancelled[/yellow]")

    except Exception as e:

        error(str(e))

        console.print(
            f"\n[red]Scan Failed : {e}[/red]"
        )


if __name__ == "__main__":
    main()