"""
This is the very first version of the SoarPro Lexer.
It takes input from the user and then returns the appropriate 
result to the user.
"""

####################################################
#################### Import ########################
####################################################
from soartokens import *


# The main Lexer Class
class SoarLexer:
  # Initialize the lexer:
  def __init__(self, text):
    self.text = text # This stands for the main source file
    self.current_char = None # Initialize the lexer with no variables
    self.pos = -1 # This tracks the position.
    #It's set to -1 because it will increase to zero as we advance and....
    #Don't forget that python's index starts from 0. So when increased it defaults to zero the beginning of the file
    
    self.advance() # Call the advance method once the lexer is initialized so as to update the current chatacter from none to the letter on the index of the position in the text

  # This methods updates the position of the lexer and the current character
  def advance(self):
    # Increase the position by 1
    self.pos += 1
    
    # Checks if we are not at the end of the file.
    # If we are at the end of the file it turns the current character to None
    if self.pos < len(self.text):
      self.current_char = self.text[self.pos]
    else:
      self.current_char = None

  # The method belows recognises the tokens and validate them
  def tokenize(self):
    tokens = [] # Store whatever token found in this list

    # Create a while loop that continues until the current character turns to None. Don't forget that the current character only turns to none if we are at the end of the file
    while self.current_char != None:
      # The condition below Ignore spaces and tabs
      if self.current_char in " \t":
        self.advance() # Call the advance method that moves to the next character
      # Condition to see if the current character is a plus sign
      elif self.current_char == "+":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_PLUS, self.pos))
        self.advance()
      elif self.current_char == "-":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_MINUS, self.pos))
        self.advance()
      elif self.current_char == "*":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_MUL, self.pos))
        self.advance()
      elif self.current_char == "/":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_DIV, self.pos))
        self.advance()

      
        