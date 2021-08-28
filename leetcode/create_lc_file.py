from pathlib import Path

import click


@click.command()
@click.option("--title", prompt="Title", help="The problem title")
def create_lc_file(title):
    f_name = f'lc_{"_".join(s.lower().replace(".", "") for s in title.split())}.py'
    f = Path(__file__).resolve().parent / Path(f_name)
    f.touch()
    print(f)


if __name__ == "__main__":
    create_lc_file()
