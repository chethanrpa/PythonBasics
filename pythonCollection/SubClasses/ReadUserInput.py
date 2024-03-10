
class ReadUserInput:
    @staticmethod
    def read():
        vInput = input("Please enter your input : ")
        return "" if (vInput == "EXIT") else vInput
