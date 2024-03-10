class TypeCastTheInputType:

    @staticmethod
    def typeCastInput(vInput):
        vInput = str.lower(vInput)  # convert the string to lower case
        if vInput == "true" or vInput == "false":  # if the input is boolean type
            return bool(vInput)
        elif vInput.isnumeric():  # if input is number
            return int(vInput)
        elif vInput.count(".") == 1 and vInput.replace(".", "").isnumeric():  # if the input is float type
            return float(vInput)
        else:  # input type is string
            return str(vInput)
