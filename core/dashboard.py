from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import platform
import socket
import getpass

console = Console()


def show_dashboard():

    table = Table(show_header=False)

    table.add_row("👤 User", getpass.getuser())
    table.add_row("💻 Host", socket.gethostname())
    table.add_row("🖥 OS", platform.system())
    table.add_row("⚙ Version", platform.version())
    table.add_row("🐍 Python", platform.python_version())

    console.print()

    console.print(
        Panel.fit(
            table,
            title="[cyan]System Information[/cyan]",
            border_style="green"
        )
    )
    