import unittest
from app import Figure


class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.square = Figure("квадрат", 5)
        self.rectangle = Figure("прямокутник", 10)
        self.triangle = Figure("трикутник", 3)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.square.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.square.get_figure_length)

    def test_get_angles(self):
        self.assertEqual(4, self.square.get_angles)
        self.assertEqual(4, self.rectangle.get_angles)
        self.assertEqual(3, self.triangle.get_angles)

    def test_unknown_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_zero_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("трикутник", -5)


if __name__ == "__main__":
    unittest.main(verbosity=2)