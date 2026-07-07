import typer

app = typer.Typer()


@app.command()
def username(name: str):
    print(f"Searching Username : {name}")
