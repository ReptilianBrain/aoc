import re

from aoc2023.utils import read_txt_file

mapping = {
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


def total(values):
    _total = 0
    for _cal in values:
        _total += _cal["number"]
    return _total


def convert_value_to_number(value) -> str:
    try:
        v = int(value)
    except ValueError:
        v = int(mapping.get(value))
    return str(v)


def parse_calibration(pattern, calibration):
    return re.findall(pattern, calibration)


if __name__ == "__main__":
    numbers_part_one = []
    numbers_part_two = []

    calibration_values = read_txt_file("1_puzzle_input.txt")

    for cal in calibration_values[1:]:
        number = parse_calibration("\\d", cal)
        numbers_part_one.append(
            {
                "calibration_value": cal,
                "number": int(number[0] + number[-1]),
            }
        )

    print(total(numbers_part_one))

    for cal in calibration_values[1:]:
        regex = re.compile("(?=(\\d|" + "|".join(mapping.keys()) + "))")
        number = parse_calibration(regex, cal)
        numbers_part_two.append(
            {
                "calibration_value": cal,
                "number": int(
                    convert_value_to_number(number[0])
                    + convert_value_to_number(number[-1])
                ),
            }
        )

    print(total(numbers_part_two))
