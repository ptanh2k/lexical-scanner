class LexicalScanner:
    def tokenizer(self, lines):
        tokens = []

        keywords = ['if', 'then', 'else', 'for', 'while', 'do', 'return']

        for line in lines:
            if (len(line) > 0):
                if (line[0] == '/' and line[1] == '/'):
                    continue
                else:
                    print(line)
            else:
                continue