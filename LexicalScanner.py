import re
from typing import NamedTuple

class LexicalScanner(NamedTuple):
    type: str
    value: str
    line: int
    column: int

    def tokenizer(self, code):
        keywords = {'if', 'then', 'else', 'for', 'while', 'do', 'return'}

        token_rules = [
            ('Identifier', r'[A-Za-z]+'),       # Identifier
            ('Digit', r'\d+(\.\d*)?'),          # Integer or decimal number
            ('End', r';'),                      # Statement terminator
            ('Newline', r'\n'),                 # End of line
            ('Skip', r'[\t]+'),                 # Space and Tab
            ('Mismatch', r'.')                  # Any other character
        ]

        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_rules)

        # Token row
        line_num = 1

        line_start = 0

        for mo in re.finditer(tok_regex, code):
            tok_type = mo.lastgroup
            lexeme = mo.group(tok_type)

            if tok_type == 'Newline':
                line_start = mo.end()
                line_num += 1
            elif tok_type == 'Skip':
                continue
            elif tok_type == 'Mismatch':
                raise RuntimeError('%r unexpected on line %d' & (lexeme, line_num))



