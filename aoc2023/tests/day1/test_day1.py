import re
import unittest

from aoc2023.day1.main import convert_value_to_number, parse_calibration, total
from aoc2023.utils import read_txt_file


class TestCalibrationValues(unittest.TestCase):
    def setUp(self):
        self.input_a = read_txt_file("1_puzzle_input_a.txt")
        self.input_b = read_txt_file("1_puzzle_input_b.txt")
        self.mapping = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

    def tearDown(self):
        pass

    def test_calibration_value_a(self):
        numbers = []
        expected_result = 142
        for cal in self.input_a[1:]:
            number = parse_calibration("\\d", cal)
            numbers.append(
                {
                    "calibration_value": cal,
                    "number": int(number[0] + number[-1]),
                }
            )
        self.assertEqual(total(numbers), expected_result)

    def test_calibration_value_b(self):
        numbers = []
        expected_result = 281
        for cal in self.input_b[1:]:
            regex = re.compile("(?=(\\d|" + "|".join(self.mapping.keys()) + "))")
            number = parse_calibration(regex, cal)
            numbers.append(
                {
                    "calibration_value": cal,
                    "number": int(
                        convert_value_to_number(number[0])
                        + convert_value_to_number(number[-1])
                    ),
                }
            )
        self.assertEqual(total(numbers), expected_result)


if __name__ == "__main__":
    unittest.main()
