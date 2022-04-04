class Symbols:
    symbols = []

    ## Add new content to line
    @staticmethod
    def add_symbol(line):
        if (line not in Symbols.symbols):
            Symbols.symbols.append(line)

    ## Get content
    @staticmethod
    def get_symbols():
        return Symbols.symbols

    ## Get index if the content has already existed in message displayed
    @staticmethod
    def get_index_if_exists(line):
        length = len(Symbols.symbols)

        for i in range(0, length):
            if (line == Symbols.symbols[i]):
                return i+1
        
        return 0

    ##
    @staticmethod
    def get_index_of_identifier(line):
        length = len(Symbols.symbols)
        exists = False
        index = 0

        for i in range(0, length):
            if (line == Symbols.symbols[i]):
                exists = True
                index += 1
                break

        if exists:
            return index
        else:
            return length + 1

    