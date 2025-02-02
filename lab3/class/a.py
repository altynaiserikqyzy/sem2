class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Введите строку: ")

    def printString(self):
        print(self.string.upper())
