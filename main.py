import argparse

from Automaton import Automaton
from Error import Error
from Symbols import Symbols
from Output import Output
from LexicalScanner import LexicalScanner

def read_file(path):
    x = 0
    with open(path) as f:
        data=  f.readlines()
        data = [i.strip() for i in data]
        ar = []
        # print(data)
        while x < len(data):
        # for x in range(len(data)):
            if "//" in data[x]:
                ar.append(data[x].strip())
                pass

            elif "/" in data[x]:
                token = ""
                for j in range(x, len(data)):
                    token += str(data[x].strip()) 
                    x += 1 
                    if("/" in data[x]):
                        token += str(data[x].strip()) 
                        x += 1 
                        break
                ar.append(token)
            else:
                data[x] = data[x].strip()
                data[x] = data[x].split(' ')
                for i in data[x]:
                    if ";" in i:
                        token = [i[:len(i)-1], i[-1]]
                        for j in token:
                            ar += j
                    elif "," in i: 
                        token = [i[:len(i)-1], i[-1]]
                        for j in token:
                            ar += j
                    else:
                        ar.append(str(i))
            x = x + 1
    return ar

def print_identifier():
    print("Identifier: ")
    identifiers = dict()
    identifiers = Output.get_output()
    indexes = [key for key in identifiers.keys()]
    length = len(identifiers)

    if length > 0:
        for i in range(0, length):
            index = indexes[i]
            identifier = identifiers[index]

            if identifier is not None:
                print("[ {} ]".format(index) + identifier)

def print_error():
    print("Error: ")
    errors = Error.get_errors()
    length = len(errors)

    print(errors)

    if length > 0:
        for i in range(0, length):
            error = errors[i]

            if i + 1 == length:
                print("e ")
            else:
                print(", ")

def print_symbols():
    print("Symbols: ")
    symbols = []
    symbols = Symbols.get_symbols()
    length = len(symbols)

    if length > 0:
        for i in range(0, length):
            symbol = symbols[i]
            print("{} ".format(i+1) + symbol)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-i", type=str, help="File to analyze")

    args = parser.parse_args()

    code = read_file(args.path)    

    print(code)

    scanner = LexicalScanner()

    # scanner.tokenizer(code)

    # print_identifier()
    # print_symbols()
    # print_error()

    