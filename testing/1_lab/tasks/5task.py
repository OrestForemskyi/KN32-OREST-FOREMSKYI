import unittest
from unittest.mock import patch


def greet_user() -> str:
    name = input("Введіть ваше ім'я: ")
    return f"Привіт, {name}!"


class TestGreetUser(unittest.TestCase):
    @patch("builtins.input", return_value="Орест")
    def test_greet_user(self, mock_input):
        result = greet_user()
        self.assertEqual(result, "Привіт, Орест!")
        mock_input.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)