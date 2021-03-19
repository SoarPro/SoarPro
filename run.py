from soarlexer import *

def run(text):
    lexer = SoarLexer(text)
    result, error = lexer.tokenize()
    return result, error