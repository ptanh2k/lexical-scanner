from Symbols import Symbols

class Output:
    output = dict()

    @staticmethod
    def set_int(line):
        output[line] = "INT"

    @staticmethod
    def set_float(line):
        output[line] = "FLOAT"

    @staticmethod
    def set_string(line):
        output[line] = "STRING"

    @staticmethod
    def set_boolean(line):
        output[line] = "BOOLEAN"

    @staticmethod
    def set_int_identifier(line, value):
        index = 0

    @staticmethod
    def set_identifier(line, value):
        index = 0

        if (Symbols.get_index_if_exists(line) != 0):
            index = Symbols.get_index_if_exists(line)
            output[line] = "IDENTIFIER" + index
        else:
            output[line] = "IDENTIFIER" + Symbols.get_index_of_identifier(value)

    @staticmethod
    def set_int_identifier(line, value):
        index = 0

        if (Symbols.get_index_if_exists(line) != 0):
            index = Symbols.get_index_if_exists(line)
            output[line] = "IDENTIFIER INT" + index
        else:
            output[line] = "IDENTIFIER INT" + Symbols.get_index_of_identifier(value)

    @staticmethod
    def set_float_identifier(line, value):
        index = 0

        if (Symbols.get_index_if_exists(line) != 0):
            index = Symbols.get_index_if_exists(line)
            output[line] = "IDENTIFIER FLOAT" + index
        else:
            output[line] = "IDENTIFIER FLOAT" + Symbols.get_index_of_identifier(value)

    @staticmethod
    def set_comment_identifier(line, value):
        output[line] = "COMMENT"

    @staticmethod
    def get_output():
        return output