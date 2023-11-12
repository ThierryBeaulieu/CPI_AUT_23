# test_my_module.py
import unittest
import numpy as np
from decode import Decoder

class TestDecodeFunction(unittest.TestCase):
    def test_separate_binary_from_base17(self):
        decoder = Decoder()
        result = decoder.get_binary_and_base17("0100000100101000:11d48ed9dCQIc6ab6c6147d845e586da03b9")
        self.assertEqual(result, ["0100000100101000", "11d48ed9dCQIc6ab6c6147d845e586da03b9"])

    def test_convert_to_intermediate_format(self):
        decoder = Decoder()
        result = decoder.convertToIntermediateFormat("CQIa14bc0CQI429cdeCQI")
        self.assertEqual(result, "ga14bc0g429cdeg")
       
    def test_convert_to_decimal_1(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("a14bc0429cde")
        self.assertEqual(result, 345290971773084)

    def test_convert_to_decimal_2(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("aa")
        self.assertEqual(result, 180)

    def test_convert_to_decimal_3(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("ab")
        self.assertEqual(result, 181)

    def test_convert_to_decimal_4(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("g")
        self.assertEqual(result, 16)

    def test_convert_to_decimal_5(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("ag123")
        self.assertEqual(result, 914144)

    def test_convert_to_decimal_6(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("abcdefg1234567890")
        self.assertEqual(result, 520256568935960080136)

    def test_convert_to_binary_1(self):
        decoder = Decoder()
        result = decoder.convertDecimalToBinary(0)
        self.assertEqual(result, "0")

    def test_convert_to_binary_2(self):
        decoder = Decoder()
        result = decoder.convertDecimalToBinary(23984203984)
        self.assertEqual(result, "10110010101100100011110100011010000")

    def test_convert_to_binary_3(self):
        decoder = Decoder()
        result = decoder.convertDecimalToBinary(520256568935960080136)
        self.assertEqual(result, "111000011010000000010101000010000001010000011011011001110111100001000")
    
    def test_convert_binary_to_permutation_matrix(self):
        decoder = Decoder()
        result = decoder.convertBinaryToPermutationMatrix("0001100110110110")
        matrix_array = np.array([[-1,1,0,0], [0,1,-1,1], [0,-1,1,0], [1,0,0,0]])
        self.assertTrue(np.array_equal(result, matrix_array))

    def test_convert_binary_into_matrix(self):
        decoder = Decoder()
        result = decoder.convertBinaryToMatrix("000110011011011010110110")
        matrix_array = np.array([[0,0,0,1], [1,0,0,1], [1,0,1,1], [0,1,1,0], [1,0,1,1], [0,1,1,0]])
        self.assertTrue(np.array_equal(result, matrix_array))

    def test_apply_transpose(self):
        decoder = Decoder()
        binaryMatrix = np.array([[1,1,0,1], [0,1,0,1], [0,1,1,0], [0,0,0,1]])
        transpose = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
        result = decoder.applyTranspose(binaryMatrix, transpose)
        self.assertTrue(np.array_equal(result, binaryMatrix))


    # def test_transpose_matrix(self):
    #     decoder = Decoder()
    #     matrixMultiplicative = decoder.convertBinaryToMatrix("0001100110110110")
    #     binaryToDecode = decoder.convertBinaryToMatrix("0001100110110110")
    #     # decoder.
    #     self.assertEqual(result,  ["0001", "1001", "1011", "0110"])
    
    
    # def test_decode_Hello_world(self):
    #     decoder = Decoder()
    #     result = decoder.decode("0100000100101000:11d48ed9dCQIc6ab6c6147d845e586da03b9")
    #     self.assertEqual(result, "Bonjour le monde!")

if __name__ == '__main__':
    unittest.main()
