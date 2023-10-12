import typer

app = typer.Typer()

@app.command()
def date(date: str):
    typer.echo(f"The date is {date}")


if __name__ == "__main__":
    app()

