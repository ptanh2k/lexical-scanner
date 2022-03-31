import argparse

from LexicalScanner import LexicalScanner
# from FileReader import FileReader

def readFile(path):
    with open(path, "r") as reader:
        print(reader.read())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-i", type=str, help="File to analyze")

    args = parser.parse_args()

    readFile(path=args.path)