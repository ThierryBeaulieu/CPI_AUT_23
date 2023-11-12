# test_my_module.py
import unittest
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
       
    def test_convert_to_decimal(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("a14bc0429cde")
        self.assertEqual(result, 345290971773084)

    def test_convert_to_decimal(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("aa")
        self.assertEqual(result, 180)

    def test_convert_to_decimal(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("ab")
        self.assertEqual(result, 181)

    def test_convert_to_decimal(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("g")
        self.assertEqual(result, 16)

    def test_convert_to_decimal(self):
        decoder = Decoder()
        result = decoder.convertToDecimal("abcdefg1234567890")
        self.assertEqual(result, )


    # def test_convert_to_binary(self):
    #     decoder = Decoder()
    #     result = decoder.convertToBinary("a14bc0429cde")
    #     self.assertEqual(result, "10100110110101010111101101101001011110000001001101100")
    
    # def test_decode_Hello_world(self):
    #     decoder = Decoder()
    #     result = decoder.decode("0100000100101000:11d48ed9dCQIc6ab6c6147d845e586da03b9")
    #     self.assertEqual(result, "Bonjour le monde!")

if __name__ == '__main__':
    unittest.main()
