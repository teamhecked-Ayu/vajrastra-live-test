import unittest

from src.service import parse_timeout


class ParseTimeoutTests(unittest.TestCase):
    def test_parses_positive_integer(self):
        self.assertEqual(parse_timeout("30"), 30)

    def test_rejects_zero(self):
        with self.assertRaises(ValueError):
            parse_timeout("0")

    def test_rejects_negative_integer(self):
        with self.assertRaises(ValueError):
            parse_timeout("-5")

    def test_rejects_non_integer(self):
        with self.assertRaises(ValueError):
            parse_timeout("fast")


if __name__ == "__main__":
    unittest.main()
