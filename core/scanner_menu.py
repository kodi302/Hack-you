"""
Hack-You Scanner Menu
"""

from rich.console import Console
from rich.prompt import Prompt

from core.port_scanner import run_port_scan
from core.risk_engine import analyze_risk
from core.logger import info
from core.port_parser import parse_ports
from core.output import print_ports
from core.output import print_ports, print_scan_summary, timer

console = Console()


def port_menu():

    while True:

        console.clear()

        console.print("""
===============================
      PORT SCANNER
===============================

1. Fast Scan
2. Full Scan
3. Custom Ports
0. Back

""")

        choice = Prompt.ask("Choice")

        # -----------------------------
        # FAST SCAN
        # -----------------------------
        if choice == "1":

            target = Prompt.ask("Target")

            info(f"Fast Port Scan Started : {target}")

            try:

                ports = run_port_scan(target, "fast")

                console.print(ports)

                if ports:
                    analyze_risk([p["port"] for p in ports])

                info(f"Fast Port Scan Completed : {target}")

            except Exception as e:

                console.print(f"[red]{e}[/red]")

            input("\nPress Enter...")

        # -----------------------------
        # FULL SCAN
        # -----------------------------
        elif choice == "2":

            start = timer()

            target = Prompt.ask("Target")

            info(f"Full Port Scan Started : {target}")

            try:

                ports = run_port_scan(target, "full")

                print_ports(ports)

                if ports:
                    analyze_risk([p["port"] for p in ports])

                info(f"Full Port Scan Completed : {target}")

            except Exception as e:

                console.print(f"[red]{e}[/red]")

            input("\nPress Enter...")

            elapsed = timer() - start

            print_ports(ports)

            print_scan_summary(
            target,
            ports,
            elapsed
            )

        # -----------------------------
        # CUSTOM PORT SCAN
        # -----------------------------
        elif choice == "3":

            target = Prompt.ask("Target")

            port_text = Prompt.ask(
                "Enter Ports (Example: 22,80,443 or 1-1000)"
            )

            try:

                custom_ports = parse_ports(port_text)

                info(f"Custom Port Scan Started : {target}")

                ports = run_port_scan(
                    target,
                    "custom",
                    custom_ports
                )

                console.print(ports)

                if ports:
                    analyze_risk([p["port"] for p in ports])

                info(f"Custom Port Scan Completed : {target}")

            except Exception as e:

                console.print(f"[red]{e}[/red]")

            input("\nPress Enter...")

        # -----------------------------
        # BACK
        # -----------------------------
        elif choice == "0":

            break

        # -----------------------------
        # INVALID OPTION
        # -----------------------------
        else:

            console.print("[red]Invalid Option[/red]")

            input("\nPress Enter...")