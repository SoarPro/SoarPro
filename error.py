class Error:
    def __init__(self, pos, error_name, details):
        self.pos = pos
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f"{self.error_name}: {self.details}\n"
        result += f"File stdin, line {self.pos.lineno}, index {self.pos.column}"
        return result
        

class BadCharacterError(Error):
    def __init__(self, pos, char):
        super().__init__(pos, "Bad Character error", {char})
        
class FloatError(Error):
    def __init__(self, pos):
        super().__init__(pos, "Invalid float", "Only one '.' is allowed")
        
class SyntaxError(Error):
    def __init__(self, pos, message):
        super().__init__(pos, message)