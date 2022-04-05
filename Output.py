from Symbols import Symbols

class Output:
    output = dict()

    @staticmethod
    def set_keyword(line):
        Output.output[line] = 'KEYWORD'

    @staticmethod
    def set_int(line):
        Output.output[line] = "INT"

    @staticmethod
    def set_float(line):
        Output.output[line] = "FLOAT"

    @staticmethod
    def set_string(line):
        Output.output[line] = "STRING"

    @staticmethod
    def set_boolean(line):
        Output.output[line] = "BOOLEAN"

    @staticmethod
    def set_identifier(line, value):
        index = 0

        if (Symbols.get_index_if_exists(line) != 0):
            index = Symbols.get_index_if_exists(line)
            Output.output[line] = "IDENTIFIER {}".format(index)
        else:
            Output.output[line] = "IDENTIFIER {}".format(Symbols.get_index_of_identifier(value))

    @staticmethod
    def set_int_literal(line, value):
        index = 0

        if (Symbols.get_index_if_exists(line) != 0):
            index = Symbols.get_index_if_exists(line)
            Output.output[line] = "LITERAL INT {}".format(index)
        else:
            Output.output[line] = "LITERAL INT {}".format(Symbols.get_index_of_identifier(value))

    @staticmethod
    def set_float_literal(line, value):
        index = 0

        if (Symbols.get_index_if_exists(line) != 0):
            index = Symbols.get_index_if_exists(line)
            Output.output[line] = "LITERAL FLOAT {}".format(index)
        else:
            Output.output[line] = "LITERAL FLOAT {}".format(Symbols.get_index_of_identifier(value))

    @staticmethod
    def set_comment_identifier(line):
        Output.output[line] = "COMMENT"

    @staticmethod
    def set_operator_identifier(line, value):
        index = 0

        if (Symbols.get_index_if_exists(line) != 0):
            index = Symbols.get_index_if_exists(line)
            Output.output[line] = "IDENTIFIER OPERATOR {}".format(index)
        else:
            Output.output[line] = "IDENTIFIER OPERATOR {}".format(Symbols.get_index_of_identifier(value))

    @staticmethod
    def set_separator_identifier(line, value):
        index = 0

        if (Symbols.get_index_if_exists(line) != 0):
            index = Symbols.get_index_if_exists(line)
            Output.output[line] = "IDENTIFIER SEPARATOR {}".format(index)
        else:
            Output.output[line] = "IDENTIFIER SEPARATOR {}".format(Symbols.get_index_of_identifier(value))

    @staticmethod
    def get_output():
        return Output.output