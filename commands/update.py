import typer

app = typer.Typer()


@app.command()
def check():
    print("Checking for updates...")
