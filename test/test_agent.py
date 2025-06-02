import unittest
from agent import parse_sentence

class TestAgentParser(unittest.TestCase):

    def test_valid_weight_sentence(self):
        sentence = "500 gramı kilograma çevir"
        result = parse_sentence(sentence)
        expected = {
            "type": "weight",
            "from_unit": "gram",
            "to_unit": "kilogram",
            "value": 500.0
        }
        self.assertEqual(result, expected)

    def test_valid_temperature_sentence(self):
        sentence = "32 fahrenheit kaç celsius yapar"
        result = parse_sentence(sentence)
        self.assertEqual(result["type"], "temperature")
        self.assertEqual(result["from_unit"], "fahrenheit")
        self.assertEqual(result["to_unit"], "celsius")
        self.assertEqual(result["value"], 32.0)

    def test_missing_number(self):
        with self.assertRaises(ValueError):
            parse_sentence("gramı kilograma çevir")

    def test_missing_units(self):
        with self.assertRaises(ValueError):
            parse_sentence("500 birim çevir")

if __name__ == "__main__":
    unittest.main()
