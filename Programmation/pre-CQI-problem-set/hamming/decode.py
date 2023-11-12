class Decoder:

    def __init__(self):
        self.base_17_to_binary = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "a": "1010",
            "b": "1011",
            "c": "1100",
            "d": "1101",
            "e": "1110",
            "f": "1111",
            "CQI": "10000"
            }
        
    def get_binary_and_base17(self, input_string):
        return input_string.split(":")
    
    def convertToDecimal(self, base17):
        decimal = 0
        i = 0
        while i < len(base17):
            if base17[i:i+3] == "CQI":
                decimal = decimal + base17[i:i+3]
                i += 3
            else:
                decimal = decimal + base17[i]
                i += 1
        return decimal
       
    def decode(self, input_string):
        binaryAndBase17 = self.get_binary_and_base17(input_string)



if __name__ == "__main__":
    decoder = Decoder()
    decoder.decode("11d48ed9dCQIc6ab6c6147d845e586da03b9")
