from pythonCollection.SubClasses.ReadUserInput import ReadUserInput
from pythonCollection.SubClasses.TypeCastTheInputType import TypeCastTheInputType


def main():
    print("Executing the Python Collection Project")
    vReadUserInput = ReadUserInput
    vTypeCastTheInputType = TypeCastTheInputType
    print("Please type EXIT to stop inputting the data")
    while True:
        vInput = vReadUserInput.read()
        if vInput == "":
            break
        vInput = vTypeCastTheInputType.typeCastInput(vInput)
        print(type(vInput))


if __name__ == '__main__':
    main()
