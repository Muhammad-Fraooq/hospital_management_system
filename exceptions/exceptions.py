from color.color import red,reset

# Custom Exceptions
class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(f"{red}[Age Error]{reset} {message}")

class InvalidGenderError(Exception):
    def __init__(self, gender):
        super().__init__(f"{red}[Gender Error]{reset} Invalid gender entered: '{gender}'. Allowed values: Male, Female, Other.")

class InvalidDateError(Exception):
    def __init__(self, message):
        super().__init__(f"{red}[Date Error]{reset} {message}")


