import numpy as np

class Decoder:

    def __init__(self):
        self.base17 = 17
        self.base_17_to_decimal = {
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
        return sum(self.base_17_to_decimal[value] * (self.base17 ** i) for i, value in enumerate(input_string[::-1]))

    def convertDecimalToBinary(self, binaryInput: str):
        binaryResult = ""

        if binaryInput == 0:
            return "0"
               
        while binaryInput > 0:
            remainder = binaryInput % 2
            binaryResult = str(remainder) + binaryResult
            binaryInput = binaryInput // 2
        return binaryResult
    
    def convertBinaryToPermutationMatrix(self, binary: str):
        rowAndColumnLength = 4
        matrix = [[int(binary[i + j]) for j in range(rowAndColumnLength)] for i in range(0, len(binary), rowAndColumnLength)]
        return  np.linalg.inv(np.array(matrix))
    
    def convertBinaryToMatrix(self, binary: str):
        rowAndColumnLength = 4
        matrix = [[int(binary[i + j]) for j in range(rowAndColumnLength)] for i in range(0, len(binary), rowAndColumnLength)]
        return np.array(matrix)

    def applyTranspose(self, binaryMatrix, permutationMatrix):
        return np.dot(binaryMatrix, permutationMatrix)
    
    def convertMatrixToStringsOfBinary(self, binaryMatrix):
        if len(binaryMatrix) % 2 != 0:
            raise Exception("Error, impossible to convert binary to ascii")
        
        asciiChars = []
        asciiChar = ""
        i = 0
        while i < len(binaryMatrix):
            for binaryValue in binaryMatrix[i]:
                asciiChar = asciiChar + str(binaryValue)
            if i % 2 == 1:
                asciiChars.append(asciiChar)
                asciiChar = ""
            i += 1
        
        return asciiChars

    def convertStringToAscii(self, input_array_of_strings):
        asciiChars = []
        for binary in input_array_of_strings:
            decimal_value = int(binary, 2)
            ascii_character = chr(decimal_value)
            asciiChars.append(ascii_character)
        return ascii_character
    
    def concatenate(self, arrayOfAsciis):
        return ''.join(arrayOfAsciis)

    def decode(self, input_string):
        # ['0100000100101000', 'ab082c29CQI']
        binaryAndBase17 = self.get_binary_and_base17(input_string)

        # ab082c29CQI -> ab082c29g
        base17IntermediateFormat = self.convertToIntermediateFormat(binaryAndBase17[1])

        # ab082c29g -> 74282885414
        base17InBinaryFormat = self.convertToDecimal(base17IntermediateFormat)

        # 74282885414 -> 1000101001011100110101110000100100110
        binaryBase2Format = self.convertDecimalToBinary(base17InBinaryFormat)

        # 0100 0001 0010 1000 -> [[-1,1,0,0], [0,1,-1,1], [0,-1,1,0], [1,0,0,0]]
        permutationMatrix = self.convertBinaryToPermutationMatrix(binaryAndBase17[0])

        # 1000 1010 0101 1....0001 0010 0110 -> [[1,0,0,0], [1,0,1,0], ...]
        resultingMatrix = self.convertBinaryToMatrix(binaryBase2Format)

        # [[-1,1,0,0] ...] * [[1,0,0,0], ...] = [[1,0,1,0], [0,1..]]
        baseMatrix = self.applyTranspose(resultingMatrix, permutationMatrix)

        # [[1,0,1,0], [0,1..]] = ['1010','01...]
        binariesStrignified = self.convertMatrixToStringsOfBinary(baseMatrix)

        # ['1010','01...] -> ['a', 'b' ..]
        asciis = self.convertStringToAscii(binariesStrignified)

        # ['a', 'b' ..] -> 'ab'
        return self.concatenate(asciis)


if __name__ == "__main__":
    decoder = Decoder()
    result = decoder.decode("0100000100101000:11d48ed9dCQIc6ab6c6147d845e586da03b9")
