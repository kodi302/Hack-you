import typer

from commands.scan import app as scan_app
from commands.info import app as info_app
from commands.dns import app as dns_app
from commands.web import app as web_app
from commands.osint import app as osint_app
from commands.update import app as update_app

app = typer.Typer()

app.add_typer(scan_app, name="scan")
app.add_typer(info_app, name="info")
app.add_typer(dns_app, name="dns")
app.add_typer(web_app, name="web")
app.add_typer(osint_app, name="osint")
app.add_typer(update_app, name="update")

if __name__ == "__main__":
    app()
