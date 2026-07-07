import typer
from core.engine import ScanEngine
from modules.network.port_scan import scan

app = typer.Typer()


@app.command()
def port(target: str):

    engine = ScanEngine()

    result = engine.run(scan, [target])

    print(result)
