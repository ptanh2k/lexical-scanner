from Output import Output
from Symbols import Symbols
from Error import Error

class Automaton:
    keywords = ['if', 'then', 'else', 'for', 'while', 'do', 'return', 'int', 'float', 'boolean', 'string', 'void', 'main()']
    operators = ['+', '-', '%', '/', '=', '>', '<', '>=', '<=', '&&', '||', '==']
    separators = [',', ';', '(', ')', '{', '}', '[', ']']

    ## Check if input is a keyword
    def is_keyword(self, input):
        return (input in self.keywords)

    ## Check if input is a int
    def is_integer(self, input):
        return input.isdigit()

    ## Check if input is float
    def is_float(self, input):
        try:
            float(input)
            return True
        except ValueError:
            return False

    ## Check if input is a operator
    def is_operator(self, input):
        return (input in self.operators)

    ## Check if input is a separator
    def is_separator(self, input):
        return (input in self.separators)

    ## Check if input is all alphabet characters
    def is_var(self, input):
        return (not self.is_keyword(input) and not self.is_integer(input) and not self.is_float(input) and not self.is_separator(input) and not self.is_operator(input))

    def float_literal(self, line, line_number):
        print("Float literal")
        if (self.is_float(line)):
            Output.set_float_literal(line_number, line)
            Symbols.add_symbol(line)
        else:
            Error.add_error(line_number)

    ## Identify number
    def int_literal(self, line, line_number):
        print("Int literal")
        if (self.is_integer(line)):
            Output.set_int_literal(line_number, line)
            Symbols.add_symbol(line)
        else:
            Error.add_error(line_number)

    ## Identify keywords
    def keyword_identifier(self, line, line_number):
        print("Keyword identifier")
        Symbols.add_symbol(line)
        Output.set_keyword(line_number)

    ## Identify comment
    def comment_identifier(self, line, line_number):
        print("Comment identifier")
        length = len(line)

        if line[1] == '*' or line[1] == '/':
            if line[length - 2] != '*':
                Error.add_error(line_number)
            else:
                if line[length - 1] != '/':
                    Error.add_error(line_number)
                else:
                    Output.set_comment_identifier(line_number)
        else:
            Error.add_error(line_number)

    ## Identify operators
    def operator_identifier(self, line, line_number):
        print("Operator identifier")
        Output.set_operator_identifier(line_number, line)
        Symbols.add_symbol(line)

    ## Identify separators
    def separator_identifier(self, line, line_number):
        print("Separator identifier")
        Output.set_separator_identifier(line_number, line)
        Symbols.add_symbol(line)

    ## Identify variable name
    def var_identifier(self, line, line_number):
        print("Variable identifier")
        Output.set_var_identifier(line_number, line)
        Symbols.add_symbol(line)

    ## Identify underline
    def underline_identifier1(self, line, line_number):
        print("Underline identifier")
        length = len(line)

        if (self.is_char(line[1]) or self.is_number(line[1])):
            if length == 2:
                Output.set_identifier(line_number, line)
                Symbols.add_symbol(line)
            else:
                self.underline_identifier2(line, line_number)
    
    def underline_identifier2(self, line, line_number):
        length = len(line)
        error = False

        for i in range(2, length):
            if (not self.is_char(line[i]) and not self.is_number(line[i])):
                Error.add_error(line_number)
                error = True
                break

        if (error == False):
            Symbols.add_symbol(line)
            Output.set_identifier(line_number, line)

    # Identify character
    def identify_character(self, line, line_number):
        if (line != ''):
            if self.is_keyword(line):
                self.keyword_identifier(line, line_number)
            elif (self.is_integer(line)):
                self.int_literal(line, line_number)
            elif (self.is_float(line)):
                self.float_literal(line, line_number)
            elif (self.is_operator(line)):
                self.operator_identifier(line, line_number)
            elif (self.is_separator(line)):
                self.separator_identifier(line, line_number)
            else:
                first_char = line[0]
                
                if first_char == '_':
                    self.underline_identifier1(line, line_number)
                elif first_char == '/':
                    self.comment_identifier(line, line_number)
                else:
                    self.var_identifier(line, line_number)