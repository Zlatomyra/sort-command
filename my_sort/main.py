import click

__version__ = "0.0.3"

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-r', '--reverse', is_flag=True)
@click.option('-n', '--numeric', is_flag=True)
@click.version_option(__version__, '--version')
def main(filename, reverse, numeric):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f]

        if numeric:
            try:
                lines = sorted(lines, key=float, reverse=reverse)
            except ValueError:
                click.echo("Нечислові дані")
                return
        else:
            lines = sorted(lines, reverse=reverse)

        for line in lines:
            click.echo(line)

    except Exception:
        click.echo("Помилка при читанні файлу")

if __name__ == "__main__":
    main()
