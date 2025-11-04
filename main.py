import typer
from rich import print
import utils.operators as operators  # <- clearer alias

app = typer.Typer()

@app.command()
def version():
    print("xyrculator version [bold red]pre:[green]0.1")

@app.command()
def multiply(a: int, b: int):
    print(operators.multiply(a, b))
@app.command()
def divide(a: int, b:int):
    print(operators.divide(a,b))
if __name__ == "__main__":
    app()
