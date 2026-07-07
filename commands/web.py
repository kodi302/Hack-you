import typer

app = typer.Typer()


@app.command()
def scan(url: str):
    print(f"Scanning Website : {url}")
