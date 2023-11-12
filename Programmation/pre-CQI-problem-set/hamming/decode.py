class Decoder:

    def __init__(self):
        self.base_17_to_decimal = {
            "0":"0",
            "1":"1",
            "2":"2",
            "3":"3",
            "4":"4",
            "5":"5",
            "6":"6",
            "7":"7",
            "8":"8",
            "9":"9",
            "a":"10",
            "b":"11",
            "c":"12",
            "d":"13",
            "e":"14",
            "f":"15",
            "CQI":"16"
            }
       
    def decode(self, input_string):
        charactersFound = ""
        i = 0
        while i < len(input_string):
            if input_string[i:i+3] == "CQI":
                charactersFound = charactersFound+input_string[i:i+3]
                i += 3
            else:
                charactersFound = charactersFound+input_string[i]
                i += 1
        return charactersFound


if __name__ == "__main__":
    decoder = Decoder()
    decoder.decode("11d48ed9dCQIc6ab6c6147d845e586da03b9")
