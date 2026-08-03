"""
Hack-You Professional Risk Engine
---------------------------------
Author : Hack-You Team
Version: 3.0
"""

from rich.console import Console
from rich.table import Table

console = Console()

# Common port risk database
RISK_DATABASE = {
    21: ("HIGH", "FTP - Unencrypted file transfer"),
    22: ("LOW", "SSH - Secure Remote Access"),
    23: ("CRITICAL", "Telnet - Insecure Remote Access"),
    25: ("MEDIUM", "SMTP - Mail Service"),
    53: ("LOW", "DNS Service"),
    80: ("MEDIUM", "HTTP - Unencrypted Web Server"),
    110: ("MEDIUM", "POP3 Mail"),
    139: ("HIGH", "NetBIOS"),
    143: ("LOW", "IMAP"),
    443: ("LOW", "HTTPS"),
    445: ("CRITICAL", "SMB - Windows File Sharing"),
    3306: ("HIGH", "MySQL Database"),
    3389: ("HIGH", "Remote Desktop (RDP)"),
    8080: ("LOW", "HTTP Alternate"),
}


def calculate_score(level):
    scores = {
        "CRITICAL": 10,
        "HIGH": 8,
        "MEDIUM": 5,
        "LOW": 2,
        "INFO": 1,
    }
    return scores.get(level, 0)


def analyze_risk(open_ports):
    """
    Analyze the risk level of open ports.
    open_ports should be a list of port numbers.
    Example:
        [22, 80, 443]
    """

    console.print("\n[bold cyan]Risk Analysis[/bold cyan]")

    if not open_ports:
        console.print("[yellow]No open ports found.[/yellow]")
        return []

    table = Table(title="Risk Report")

    table.add_column("Port", justify="center", style="cyan")
    table.add_column("Severity", justify="center")
    table.add_column("Score", justify="center")
    table.add_column("Description")

    report = []

    for port in sorted(open_ports):

        severity, description = RISK_DATABASE.get(
            port,
            ("INFO", "Unknown Service")
        )

        score = calculate_score(severity)

        report.append({
            "port": port,
            "severity": severity,
            "score": score,
            "description": description,
        })

        color = {
            "CRITICAL": "red",
            "HIGH": "bright_red",
            "MEDIUM": "yellow",
            "LOW": "green",
            "INFO": "cyan",
        }.get(severity, "white")

        table.add_row(
            str(port),
            f"[{color}]{severity}[/{color}]",
            str(score),
            description,
        )

    console.print(table)

    total_score = sum(item["score"] for item in report)

    console.print(
        f"\nOverall Risk Score : [bold]{total_score}[/bold]"
    )

    if total_score >= 40:
        console.print(
            "[bold red]Overall Risk Level : CRITICAL[/bold red]"
        )

    elif total_score >= 25:
        console.print(
            "[bold bright_red]Overall Risk Level : HIGH[/bold bright_red]"
        )

    elif total_score >= 10:
        console.print(
            "[bold yellow]Overall Risk Level : MEDIUM[/bold yellow]"
        )

    else:
        console.print(
            "[bold green]Overall Risk Level : LOW[/bold green]"
        )

    return report