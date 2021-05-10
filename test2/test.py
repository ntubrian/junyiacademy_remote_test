import unittest
from main import num_generator

class TestRever(unittest.TestCase):
    def test_num_generator(self):
        self.assertEqual(num_generator(15, 3, 5), 9)
        self.assertEqual(num_generator(100, 3, 4), 58)
        self.assertEqual(num_generator(1000, 23, 29), 925)
        self.assertEqual(num_generator(1234234, 11, 13), 1044352)
        self.assertEqual(num_generator(3321, 123, 321), 3284)
        self.assertEqual(num_generator(342321, 451, 123), 338791)
        self.assertEqual(num_generator(872113, 41, 97), 842290)
        self.assertEqual(num_generator(213235246, 4231, 124355), 213183134)
        self.assertEqual(num_generator(97328454292234, 12345676, 32434546745), 97328446405628)
        self.assertEqual(num_generator(11111111111111111, 23, 43), 10392090776317267)


if __name__ == "__main__":
    unittest.main()
