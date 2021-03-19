class Error:
    def __init__(self, pos, details):
        self.pos = pos
        self.details = details

    def as_string(self):
        return f"""
Error on line {self.pos.lineno} index {self.pos.column}:
  {self.details}
        """

class BadCharacterError(Error):
    def __init__(self, pos, char):
        super().__init__(pos, f"Found a mystery character: {char!r}")
        
class FloatError(Error):
    def __init__(self, pos):
        super().__init__(pos, f"Invalid float! Only one '.' is allowed in a float")