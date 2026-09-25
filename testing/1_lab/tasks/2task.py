import unittest


def count_vowels(text: str) -> int:
    vowels = set("аеєиіїоуюяaeiouАЕЄИІЇОУЮЯAEIOU")
    return sum(1 for char in text if char in vowels)


class TestCountVowels(unittest.TestCase):
    def test_standard_string(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_digits_and_symbols(self):
        self.assertEqual(count_vowels("12345!@#"), 0)

    def test_ukrainian_letters(self):
        self.assertEqual(count_vowels("Привіт світ"), 3)
        self.assertEqual(count_vowels("Яблуко"), 3)


if __name__ == "__main__":
    unittest.main()