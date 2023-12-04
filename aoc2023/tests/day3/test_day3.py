import unittest

from aoc2023.day2.main import parse_game, puzzle_a, puzzle_b
from aoc2023.utils import read_txt_file


class TestCalibrationValues(unittest.TestCase):
    def setUp(self):
        self.input_ = read_txt_file("2_puzzle_input_test.txt")[1:]
        self.baseline = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

    def tearDown(self):
        pass

    def test_game_total_a(self):
        expected_result = 8
        games_result = parse_game(self.input_)
        total = puzzle_a(games_result)

        self.assertEqual(expected_result, total)

    def test_calibration_value_b(self):
        expected_result = 2286
        games_result = parse_game(self.input_)
        total = puzzle_b(games_result)

        self.assertEqual(expected_result, total)


if __name__ == "__main__":
    unittest.main()
