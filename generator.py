import string,random

class Generator():

    def __init__(self):
        self.__lower = True
        self.__upper = True
        self.__numbers = True
        self.__special_char = False
        self.__length = 16

# Getters & Setters
    def check(self):
        if self.get_length() < 6:
            return 'Invalid'
        if self.__lower:
            return True
        elif self.__upper:
            return True
        elif self.__special_char:
            return True
        elif self.__numbers:
            return True
        else:
            return False

    def get_lower(self):
        return self.__lower

    def set_lower(self, value):
        self.__lower = value

    def get_upper(self):
        return self.__upper

    def set_upper(self, value):
        self.__upper = value

    def get_numbers(self):
        return self.__numbers

    def set_numbers(self, value):
        self.__numbers = value

    def get_special_char(self):
        return self.__special_char

    def set_special_char(self, value):
        self.__special_char = value

    def get_length(self):
        return self.__length

    def set_length(self, value):
        self.__length = value

    def generate(self):
        characters = []

        if self.check() == True:
            if self.get_lower():
                characters += string.ascii_lowercase

            if self.get_numbers():
                characters += string.digits

            if self.get_upper():
                characters += string.ascii_uppercase

            if self.get_special_char():
                characters += string.punctuation

            new_password =''
            for each in range(1,self.get_length()):
                new_password += random.choice(characters)

            return new_password
        elif self.check() == 'Invalid':
            raise InvalidLengthError("Invalid Length")
        else:
            raise GenFail("Fakse")


class InvalidLengthError(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

class GenFail(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}
