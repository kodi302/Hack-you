from rich.console import Console
from rich.panel import Panel
import platform
import sys

console = Console()


def show():

    banner = r"""
██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝
███████║███████║██║     █████╔╝
██╔══██║██╔══██║██║     ██╔═██╗
██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

    console.print(
        Panel.fit(
            banner,
            title="Hack-You v2.0",
            subtitle="Professional Cybersecurity Toolkit",
            border_style="green"
        )
    )

    console.print(f"Python : {sys.version.split()[0]}")
    console.print(f"OS      : {platform.system()}")
    console.print(f"Machine : {platform.machine()}")


# Backward compatibility
show_banner = show