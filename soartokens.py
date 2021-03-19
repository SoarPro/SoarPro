"""
Quick Note:
  The TT prefix in the token names stands for Token Type

"""

####################################################
############## Constants ###########################
####################################################
DIGITS = "0123456789"

####################################################
############## Data Types###########################
####################################################
TT_INT = "TT_INT" # integers 0-9, e.g: 134
TT_FLOAT = "TT_FLOAT" # floats 0-9.0-9., e.g: 32.45
TT_STRING = "TT_STRING" # string, e.g: "XLang is the best"


####################################################
############## Operators############################
####################################################
TT_DIV = "DIV" # division symbol "/"
TT_MUL = "MUL" # multiplication symbol "*"
TT_PLUS = "PLUS" # addition symbol "+"
TT_MINUS = "MINUS" # minus symbol "-"

####################################################
############## Symbols #############################
####################################################
TT_LPAREN = "LPAREN" # left parentheses "("
TT_RPAREN = "RPAREN" # right parentheses ")"
# TT_LBRACE = "LBRACE" # left brace "{"
# TT_RBRACE = "RBRACE" # right brace "}"
# TT_LSBRACE = "LSBRACE" # left square brace "["
# TT_RSBRACE = "RSBRACE" # right square brace "]"


####################################################
################# Token Class ######################
####################################################

class Token:
    # Initialize the class with three variables
    # Type, Position and Value
    def __init__(self, _type, pos, value=None):
        self.type = _type
        self.pos = pos
        self.value = value

    # This methods create a representation of this class as a string
    def __repr__(self):
        # If value was given
        if self.value:
            return f"{self.type}: {self.value}"
        # Do this if value wasn't given
        else:
            return f"{self.type}"