from rich.console import Console
from rich.panel import Panel
import platform
import sys

console = Console()


def show_banner():

    banner = r"""

██╗  ██╗ █████╗  ██████╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
███████║███████║██║     █████╔╝      ╚████╔╝ ██║   ██║██║   ██║
██╔══██║██╔══██║██║     ██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║
██║  ██║██║  ██║╚██████╗██║  ██╗       ██║   ╚██████╔╝╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝

"""

    console.print(
        Panel.fit(
            banner,
            title="[cyan]Hack-You v2.0[/cyan]",
            subtitle="Professional Cybersecurity Toolkit",
            border_style="green",
        )
    )

    console.print(f"[cyan]Python :[/cyan] {sys.version.split()[0]}")
    console.print(f"[cyan]OS      :[/cyan] {platform.system()}")
    console.print(f"[cyan]Machine :[/cyan] {platform.machine()}")