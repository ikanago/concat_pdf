import PyPDF2
import click


@click.command()
@click.option("-d", "--directory", type=click.Path(exists=True), help="Directory to store files to be concatenated")
@click.option("-o", "--output", type=click.Path(), default="output.pdf", help="Concatenated file name")
def cmd(directory, output):
    print(directory)
    print(output)

def main():
    cmd()

if __name__ == "__main__":
    main()
