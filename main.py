import argparse

from Automaton import Automaton
from Error import Error
from Symbols import Symbols
from Output import Output

def read_file(path):
    with open(path, "r") as reader:
        lines = [line.strip() for line in reader]

    return lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-i", type=str, help="File to analyze")

    args = parser.parse_args()

    code = read_file(args.path)

    scanner = Automaton()

    scanner.tokenizer(code)