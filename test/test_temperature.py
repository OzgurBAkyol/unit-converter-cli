import unittest
import temperature

class TestTemperatureConversion(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(temperature.convert("celsius", "fahrenheit", 0), 32.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(temperature.convert("fahrenheit", "celsius", 32), 0.0)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(temperature.convert("kelvin", "celsius", 273.15), 0.0)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(temperature.convert("celsius", "kelvin", 100), 373.15)

    def test_invalid_from_unit(self):
        with self.assertRaises(ValueError):
            temperature.convert("rankine", "celsius", 100)

    def test_invalid_to_unit(self):
        with self.assertRaises(ValueError):
            temperature.convert("celsius", "delisle", 100)

    def test_santigrat_to_fahrenheit(self):
        result = temperature.convert("santigrat", "fahrenheit", 100)
        self.assertAlmostEqual(result, 212.0, places=1)

if __name__ == "__main__":
    unittest.main()
