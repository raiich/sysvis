"""System visualization/animation tool.

usage:
  sysvis [-i <file>] [-o <svg>]
  sysvis -h | --help

Options:
  -h --help     show help
  -i <file>     specify input sysvis file name
  -o <svg>      specify output SVG file name
"""

from docopt import docopt

from sysvis import example
from sysvis.parser import parse


def main():
    args = docopt(__doc__)
    convert(args.get('-i'), args.get('-o') or 'a')


def convert(infile, outfile):
    if infile:
        with open(infile, 'r') as f:
            statement = f.read()
    else:
        statement = example.example_statement

    story = parse(statement)
    story.play(outfile)


if __name__ == '__main__':
    main()
