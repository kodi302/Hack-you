import typer
import platform
import socket

app = typer.Typer()


@app.command()
def system():

    print("OS :", platform.system())
    print("Release :", platform.release())
    print("Machine :", platform.machine())
    print("Hostname :", socket.gethostname())
