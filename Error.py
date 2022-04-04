class Error:
    errors = []

    @staticmethod
    def add_error(line):
        Error.errors.append(line)

    @staticmethod
    def get_errors():
        return Error.errors