import unittest

from aoc2023.day4.main import part_1, part_2
from aoc2023.utils import read_txt_file


class TestCalibrationValues(unittest.TestCase):
    def setUp(self):
        self.input_ = read_txt_file("4_puzzle_input_test.txt")

    def tearDown(self):
        pass

    def test_game_total_a(self):
        expected_result = 13
        games_result = part_1(self.input_)

        self.assertEqual(expected_result, games_result)

    def test_calibration_value_b(self):
        expected_result = 30
        games_result = part_2(self.input_)
        self.assertEqual(expected_result, games_result)


if __name__ == "__main__":
    unittest.main()
