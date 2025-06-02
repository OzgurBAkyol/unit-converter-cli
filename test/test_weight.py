import unittest
import weight

class TestWeightConversion(unittest.TestCase):

    def test_kilogram_to_gram(self):
        self.assertEqual(weight.convert("kilogram", "gram", 1), 1000)

    def test_gram_to_kilogram(self):
        self.assertAlmostEqual(weight.convert("gram", "kilogram", 1500), 1.5)

    def test_pound_to_kilogram(self):
        self.assertAlmostEqual(weight.convert("pound", "kilogram", 2.20462), 1.0, places=1)

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            weight.convert("stone", "gram", 5)

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            weight.convert("gram", "stone", 500)

if __name__ == "__main__":
    unittest.main()
