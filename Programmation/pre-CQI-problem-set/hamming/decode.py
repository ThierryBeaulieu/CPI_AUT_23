class Decoder:

    def __init__(self):
        self.base10 = 10
        self.base_17_to_binary = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15,
            "CQI": 16,
            }
        
    def get_binary_and_base17(self, input_string):
        return input_string.split(":")
    
    def convertToIntermediateFormat(self, input_string):
        newFormat = ""
        i = 0
        while i < len(input_string):
            if input_string[i:i+3] == "CQI":
                newFormat = newFormat + "g"
                i += 3
            else:
                newFormat = newFormat + input_string[i]
                i += 1
        return newFormat
    
    # accepts only the strings already converted "CQI" -> "g"
    def inverse(self, input_string):
        stringInversed = ""
        i = 0
        while i < len(input_string):
                index = len(input_string) -1 - i
                stringInversed = stringInversed + input_string[index]
                i += 1
        return stringInversed
    
    def convertToDecimal(self, input_string):
        stringInversed = ""
        i = 0
        while i < len(input_string):
                index = len(input_string) -1 - i
                stringInversed = stringInversed + input_string[index]
                i += 1
        return stringInversed

    def convertToBinary(self, inputString):
         return "0"
       
    def decode(self, input_string):
        binaryAndBase17 = self.get_binary_and_base17(input_string)
        base17ToParse = self.convertToIntermediateFormat(binaryAndBase17[1])



if __name__ == "__main__":
    decoder = Decoder()
    decoder.decode("11d48ed9dCQIc6ab6c6147d845e586da03b9")
