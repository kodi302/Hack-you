import typer

app = typer.Typer()


@app.command()
def lookup(domain: str):
    print(f"DNS Lookup Started : {domain}")
