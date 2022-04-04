from Automaton import Automaton
class LexicalScanner:
    automaton = Automaton()

    def tokenizer(self, lines):

        line = None

        line_number = 1

        for line in lines:
            if (len(line.strip()) != 0):
                self.automaton.identify_character(line.strip(), line_number)
                line_number += 1
            else:
                continue


        