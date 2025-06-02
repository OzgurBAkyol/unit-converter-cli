import unittest
import agent

class TestAgentFallback(unittest.TestCase):

    def test_fallback_known_case(self):
        text = "2500 gram kaç kilogram eder"
        result = agent.parse_sentence(text)
        self.assertEqual(result["from_unit"], "gram")
        self.assertEqual(result["to_unit"], "kilogram")
        self.assertAlmostEqual(result["value"], 2500)

    def test_fallback_partial_sentence(self):
        text = "kaç metre var 2 kilometrede?"
        result = agent.parse_sentence(text)
        self.assertEqual(result["from_unit"], "kilometre")
        self.assertEqual(result["to_unit"], "metre")

    def test_failure_case(self):
        with self.assertRaises(ValueError):
            agent.parse_sentence("bu bir anlamsız cümle")
