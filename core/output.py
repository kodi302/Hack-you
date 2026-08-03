"""
Hack-You Professional Output Formatter
Version : 3.0
"""

import time

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def timer():
    """
    Return current high precision time.
    """
    return time.perf_counter()


def print_ports(ports):
    """
    Display scanned ports in a professional table.
    """

    if not ports:
        console.print("[bold red]No Open Ports Found[/bold red]")
        return

    table = Table(
        title="Hack-You Scan Results",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Port", justify="center", style="cyan", no_wrap=True)
    table.add_column("Service", style="green")
    table.add_column("State", justify="center", style="yellow")
    table.add_column("Banner", style="magenta")

    for item in ports:

        table.add_row(
            str(item.get("port", "")),
            item.get("service", "Unknown"),
            item.get("state", "Unknown"),
            item.get("banner", "N/A")
        )

    console.print(table)


def print_scan_summary(target, ports, elapsed):
    """
    Print scan summary.
    """

    console.print(
        Panel.fit(
            f"""
Target      : {target}
Open Ports  : {len(ports)}
Scan Time   : {elapsed:.2f} sec
Status      : Completed
""",
            title="Scan Summary",
            border_style="green"
        )
    )