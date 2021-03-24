"""
This is the very first version of the SoarPro Lexer.
It takes input from the user and then returns the appropriate 
result to the user.
"""

####################################################
#################### Import ########################
####################################################
from soartokens import *
from error import *
from position import *


####################################################
#################### Lexer ########################
####################################################
class SoarLexer:
  # Initialize the lexer:
  def __init__(self, text):
    self.text = text # This stands for the main source file
    self.current_char = None # Initialize the lexer with no variables
    self.pos = Position(-1, 1, 0) # This tracks the position.
    #It's set to -1 because it will increase to zero as we advance and....
    #Don't forget that python's index starts from 0. So when increased it defaults to zero the beginning of the file
    
    self.advance() # Call the advance method once the lexer is initialized so as to update the current chatacter from none to the letter on the index of the position in the text

  # This methods updates the position of the lexer and the current character
  def advance(self):
    # Increase the position by 1
    self.pos.advance(self.current_char)
    
    # Checks if we are not at the end of the file.
    # If we are at the end of the file it turns the current character to None
    if self.pos.index < len(self.text):
      self.current_char = self.text[self.pos.index]
    else:
      self.current_char = None

  # The method belows recognises the tokens and validate them
  def tokenize(self):
    tokens = [] # Store whatever token found in this list
    error = None # we store error

    # Create a while loop that continues until the current character turns to None. Don't forget that the current character only turns to none if we are at the end of the file
    while self.current_char != None:
      # The condition below Ignore spaces and tabs
      if self.current_char in " \t":
        self.advance() # Call the advance method that moves to the next character
      # Condition to see if the current character is a plus sign
      elif self.current_char == "\n":
        self.advance() # Call the advance method that moves to the next character
      # Condition to see if the current character is a plus sign
      elif self.current_char == "+":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_PLUS, self.pos.copy()))
        self.advance()
      elif self.current_char == "-":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_MINUS, self.pos.copy()))
        self.advance()
      elif self.current_char == "*":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_MUL, self.pos.copy()))
        self.advance()
      elif self.current_char == "/":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_DIV, self.pos.copy()))
        self.advance()
      elif self.current_char == "(":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_LPAREN, self.pos.copy()))
        self.advance()
      elif self.current_char == ")":
        # If found update the tokens list
        # Append the token with the coding instance class created in the SoarTokens class
        # And also don't forget to advance to the next token with the advance method
        tokens.append(Token(TT_RPAREN, self.pos.copy()))
        self.advance()
      elif self.current_char in DIGITS:
        # For this we would call the make number function below
        # to get the kind of number we are trying to tokenize
        result , err = self.make_number()
        if err:
          error = FloatError(self.pos.copy())
        else:
          tokens.append(result)
      elif self.current_char in "\"\'":
        # It should be able to parse strings, whether they
        # use single quotes or double quotes
        result, err = self.make_string()
        
        if err:
          error = SyntaxError(self.pos.copy(), message)
        else:
          tokens.append(result)
      else:
        error = BadCharacterError(self.pos.copy(), self.current_char)
        break
    return tokens, error
    
  def make_string(self):
    # The quote_symbol can either be single quotes or double quotes
    quote_symbol = self.current_char
    string = ""
    
    # move on to the next character after the opening quote
    self.advance()
    
    error = None
    
    # Keep adding characters to the string until we reach the
    # end of the string
    while self.current_char != quote_symbol:
      if self.current_char == None:
        error = "String does not have closing quotation mark"
        break
      elif self.current_char == "\n":
        error = "String cannot span more than one line"
        break
      else:
        string.append(self.current_char())
        self.advance()
    
    # we move on to the next character after the end of the string
    self.advance()
    
    if error:
      return None, error
    else:
      return Token(TT_STRING, self.pos.copy(), string), None
  
  def make_number(self):
    # We will first save the number as a string and change it to 
    # either a float or an integer later
    num_string = ""
    
    # We would also have to keep track of the dots... If there is any dot
    # it instead returns a float type token
    # And if also it is more than one it returns an error because
    # We cannot have more than one dot in a float
    dot_count = 0
    error = None

    # Run a while loop as far as the current character is not none and 
    # and it is in digits or it is a dot

    while self.current_char != None and self.current_char in DIGITS + ".":
      # Check if it is a dot
      # If it is a dot add it to the num string and increase
      # The dot_count variable
      # If the dot_count variable is greater than 0 break
      if self.current_char == ".":
        if dot_count == 1:
          error = "There is an error"
          
        else:
          dot_count += 1
          num_string += self.current_char
      else:
        num_string += self.current_char

      # We shouldn't forget to advance to the next character
      self.advance()

    # We would now return either a float type token or an int type depending
    # on the dot_count
    if error:
      return None, error

    elif dot_count > 0:
      return Token(TT_FLOAT, self.pos.copy(), num_string), None

    else:
      return Token(TT_INT, self.pos.copy(), num_string), None