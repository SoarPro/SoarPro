class Position:
    def __init__(self, index, lineno, column):
        # This is for tracking the position of the
        # Lexer in the whole source
        self.index = index

        # This is for tracking new lines
        self.lineno = lineno

        # This is for tracking the position of the
        # Lexer in the current line
        self.column = column

    def advance(self, current_char = None):
        # Increment the position of the lexer by one in the whole file
        self.index += 1
        # Increment the position of the lexer by one in the current line
        self.column += 1

        # Increment the lineno and reset the column back
        # To zero if its encounters newline
        if current_char == "\n":
            self.lineno += 1
            self.column += 1

        return self

    def copy(self):
        return Position(self.index, self.lineno, self.column)