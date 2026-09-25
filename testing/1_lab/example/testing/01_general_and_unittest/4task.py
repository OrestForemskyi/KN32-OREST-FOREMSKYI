import unittest
from app import Figure


class TestFigureSubTest(unittest.TestCase):
    def test_all_figure_types(self):
        figures_data = [
            ("квадрат", 4),
            ("прямокутник", 4),
            ("трикутник", 3),
        ]
        for fig_type, expected_angles in figures_data:
            with self.subTest(figure_type=fig_type):
                fig = Figure(fig_type, 5)
                self.assertEqual(fig.get_figure_type, fig_type)
                self.assertEqual(fig.get_angles, expected_angles)


if __name__ == "__main__":
    unittest.main(verbosity=2)