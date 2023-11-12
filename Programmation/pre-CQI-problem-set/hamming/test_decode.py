# test_my_module.py
import unittest
from decode import Decoder

class TestDecodeFunction(unittest.TestCase):
    def test_decode_Hello_world(self):
        decoder = Decoder()
        result = decoder.decode("0100000100101000:11d48ed9dCQIc6ab6c6147d845e586da03b9")
        self.assertEqual(result, "Bonjour le monde!")

if __name__ == '__main__':
    unittest.main()
