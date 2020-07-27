import PyPDF2
import click
import natsort
import os
from typing import List


def concat_pdf(directory: str, output: str):
    """
    Concatenate pdf files in a directory.

    ## Parameters  
    `directory`: Directory name storing pdf files  
    `output`: Name of file that concatenated pdf is written on
    """
    merger = PyPDF2.PdfFileMerger()
    files = sort_files(directory)
    for filename in files:
        merger.append(os.path.join(directory, filename))
    merger.write(output)
    merger.close()


def sort_files(directory: str) -> List[str]:
    """
    Sort files in the `directory` and return as a list.
    `["hoge/a001pdf", "hoge/a010pdf", "hoge/a020.pdf", "hoge/a002pdf"]` is sorted as
    `["hoge/a001pdf", "hoge/a002pdf", "hoge/a010.pdf", "hoge/a020pdf"]`

    ## Parameters  
    `directory`: Directory name whose file is sorted
    """

    return natsort.natsorted(os.listdir(directory))


@click.command(help="Specify directory storing files, and concatenate all of them")
@click.argument("directory", type=click.Path(exists=True))
@click.option("-o", "--output", type=click.Path(), default="output.pdf", help="Output file name")
def cmd(directory, output):
    concat_pdf(directory, output)


def main():
    cmd()


if __name__ == "__main__":
    main()
