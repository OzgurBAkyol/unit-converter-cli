import unittest
from length import convert as length_convert
from weight import convert as weight_convert
from temperature import convert as temperature_convert

class TestConverter(unittest.TestCase):
    def test_length_conversion(self):
        # Metre'den kilometre'ye dönüşüm
        result = length_convert("metre", "kilometre", 1000)
        self.assertAlmostEqual(result, 1.0)

        # Kilometre'den metre'ye dönüşüm
        result = length_convert("kilometre", "metre", 1)
        self.assertAlmostEqual(result, 1000.0)

    def test_weight_conversion(self):
        # Kilogram'dan gram'a dönüşüm
        result = weight_convert("kilogram", "gram", 1)
        self.assertAlmostEqual(result, 1000.0)

        # Gram'dan kilogram'a dönüşüm
        result = weight_convert("gram", "kilogram", 1000)
        self.assertAlmostEqual(result, 1.0)

    def test_temperature_conversion(self):
        # Celsius'dan Fahrenheit'a dönüşüm
        result = temperature_convert("celsius", "fahrenheit", 0)
        self.assertAlmostEqual(result, 32.0)

        # Fahrenheit'tan Celsius'a dönüşüm
        result = temperature_convert("fahrenheit", "celsius", 32)
        self.assertAlmostEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main() 