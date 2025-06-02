import unittest
import length

class TestLengthConversion(unittest.TestCase):

    def test_meter_to_kilometer(self):
        self.assertAlmostEqual(length.convert("meter", "kilometer", 1000), 1.0)

    def test_kilometer_to_meter(self):
        self.assertEqual(length.convert("kilometer", "meter", 1), 1000)

    def test_centimeter_to_meter(self):
        self.assertEqual(length.convert("centimeter", "meter", 100), 1)

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            length.convert("invalid", "meter", 100)

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            length.convert("meter", "invalid", 100)

if __name__ == "__main__":
    unittest.main()
