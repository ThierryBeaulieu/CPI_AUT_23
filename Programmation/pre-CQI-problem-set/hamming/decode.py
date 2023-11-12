class Decoder:

    def __init__(self):
        self.base17 = 17
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
            "g": 16,
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
    def convertToDecimal(self, input_string):
        decimalValue = 0
        i = 0
        while i < len(input_string):
                index = len(input_string) -1 - i
                decimalValue = decimalValue + self.base_17_to_binary[input_string[i]] * (self.base17 ** index) 
                i += 1
        return decimalValue

    def convertToBinary(self, inputString):
         return "0"
       
    def decode(self, input_string):
        binaryAndBase17 = self.get_binary_and_base17(input_string)
        base17ToParse = self.convertToIntermediateFormat(binaryAndBase17[1])



if __name__ == "__main__":
    decoder = Decoder()
    result = decoder.convertToDecimal("ab")
