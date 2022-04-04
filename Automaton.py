from Output import Output
from Symbols import Symbols
from Error import Error

class Automaton:
    keywords = ['if', 'then', 'else', 'for', 'while', 'do', 'return', 'int', 'float', 'string', 'char', 'void', 'main()']

    ## Check if input is a number
    def is_number(self, input):
        return input.isdigit()

    ## Check if input is all alphabet characters
    def is_char(self, input):
        return input.isalpha()

    def num_identifier(self, line, line_number):
        length = len(line)
        is_float = False
        error = False

        for i in range(2, length):
            if (not self.is_number(line[i])):
                if (line[i] != '.'):
                    Error.add_error(line_number)
                    error = True
                    break
                else:
                    if (length < (i + 2)):
                        Error.add_error(line_number)
                        error = True
                        break
                    else:
                        if (not is_number(line[i + 1])):
                            Error.add_error(line_number)
                            error = True
                            break
                        is_float = True

        if error == False:
            Symbols.add_symbol(line)
            if (is_float):
                Output.set_float_identifier(line_number, line)
            else:
                Output.set_int_identifier(line_number, line)

    ## Identify number
    def number_identifier(self, line, line_number):
        print("Number identifier")
        if (self.is_number(line[1])):
            if len(line) == 2:
                Output.set_int_identifier(line_number, line)
                Symbols.add_symbol(line)
            else:
                self.num_identifier(line, line_number)
        else:
            Error.add_error(line_number)

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

    ## Identify integer
    def int_identifier(self, line, line_number):
        print("Int identifier")
        length = len(line)
        error = False

        if (length <= 5):
            for i in range(1, length):
                if i == 1:
                    if line[i] == 'n':
                        error = False
                    else:
                        error = True

                elif i == 2:
                    if line[i] == 't':
                        error = False
                    else:
                        error = True
                else:
                    error = True

                if (error):
                    Error.add_error(line_number)
                    break

        else:
            error = True
            Error.add_error(line_number)

        if error == False:
            Output.set_int(line_number)

    ## Identify float
    def float_Identifier(self, line, line_number):
        print('Float_Identifier')
        length = len(line)
        error = False

        if (length <= 5):
            for i in range(1, length):
                if i == 1:
                    if line[i] == 'l':
                        error = False
                    else:
                        error = True

                elif i == 2:
                    if line[i] == 'o':
                        error = False
                    else:
                        error = True
                elif i == 3:
                    if line[i] == 'a':
                        error = False
                    else:
                        error = True
                elif i == 4:
                    if line[i] == 't':
                        error = False
                    else:
                        error = True
                else:
                    error = True

                if (error):
                    Error.add_error(line_number)
                    break

        else:
            error = True
            Error.add_error(line_number)

        if error == False:
            Output.set_float(line_number)

    ## Identify char
    def char_identifier(self, line, line_number):
        print("Char identifier")
        length = len(line)
        error = False

        if (length <= 4):
            for i in range(1, length):
                if i == 1:
                    if line[i] == 'h':
                        error = False
                    else:
                        error = True

                elif i == 2:
                    if line[i] == 'a':
                        error = False
                    else:
                        error = True
                elif i == 3:
                    if line[i] == 'r':
                        error = False
                    else:
                        error = True
                else:
                    error = True

                if (error):
                    Error.add_error(line_number)
                    break

        else:
            error = True
            Error.add_error(line_number)

        if error == False:
            Output.set_string(line_number)

    ## Identify boolean
    def boolean_identifier(self, line, line_number):
        print("Boolean identifier")
        length = len(line)
        error = False

        if (length <= 7):
            for i in range(1, length):
                if i == 1:
                    if line[i] == 'o':
                        error = False
                    else:
                        error = True

                elif i == 2:
                    if line[i] == 'o':
                        error = False
                    else:
                        error = True
                elif i == 3:
                    if line[i] == 'l':
                        error = False
                    else:
                        error = True
                elif i == 4:
                    if line[i] == 'e':
                        error = False
                    else:
                        error = True
                elif i == 5:
                    if line[i] == 'a':
                        error = False
                    else:
                        error = True
                elif i == 6:
                    if line[i] == 'n':
                        error = False
                    else:
                        error = True
                else:
                    error = True

                if (error):
                    Error.add_error(line_number)
                    break

        else:
            error = True
            Error.add_error(line_number)

        if error == False:
            Output.set_boolean(line_number)


    ## Identify comment
    def comment_identifier(self, line, line_number):
        print("Comment identifier")
        length = len(line)

        if line[1] == '*':
            if line[length - 2] != '*':
                Error.add_error(line_number)
            else:
                if line[length - 1] != '/':
                    Error.add_error(line_number)
                else:
                    Output.set_comment_identifier(line_number, line)
        else:
            Error.add_error(line_number)

    # Identify character
    def identify_character(self, line, line_number):
        if (line != ''):
            if (self.is_number(line[0])):
                self.number_identifier(line, line_number)
            else:
                first_char = line[0]
                
                if first_char == '_':
                    self.underline_identifier1(line, line_number)
                elif first_char == '-':
                    self.number_identifier(line, line_number)
                elif first_char == '+':
                    self.number_identifier(line, line_number)
                elif first_char == '/':
                    self.comment_identifier(line, line_number)
                elif first_char == 'i':
                    self.int_identifier(line, line_number)
                elif first_char == 'f':
                    self.float_identifier(line, line_number)
                elif first_char == 'c':
                    self.char_identifier(line, line_number)
                elif first_char == 'b':
                    self.boolean_identifier(line, line_number)
                else:
                    Error.add_error(line_number)