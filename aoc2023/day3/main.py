import re
from aoc2023.utils import read_txt_file

from pprint import pprint


def parse_calibration(pattern, calibration):
    return re.findall(pattern, calibration)


def total(values):
    _total = 0
    for _cal in values:
        _total += _cal
    return _total


def part1(schematic):
    symbols = set(
        parse_calibration(r"[^.|\d]", ".".join([x.rstrip("\n") for x in schematic]))
    )
    valid_value = []
    for idx, _row in enumerate(schematic):
        row = _row.rstrip("\n")

        for n in re.finditer("\\d+", row):
            numb = int(n.group())
            print(f"processing: {n.group()}")
            start = n.start()
            end = len(n.group())
            # what's left?
            if start != 0 and row[start - 1] in symbols:
                valid_value.append(numb)
            # what's right?
            if (start + end) != len(row) and row[start + end] in symbols:
                valid_value.append(numb)
            # what's down ?
            start = 1 if start == 0 else start
            if idx != len(schematic) - 1:
                for x in schematic[idx + 1][start - 1: start + end + 1]:
                    if x in symbols:
                        valid_value.append(numb)
            # what's up ?
            if idx != 0:
                for x in schematic[idx - 1][start - 1: start + end + 1]:
                    if x in symbols:
                        valid_value.append(numb)
    return valid_value


if __name__ == "__main__":
    schematic = read_txt_file("3_puzzle_input.txt")
    # schematic = read_txt_file("3_puzzle_input_test.txt")

    pprint(schematic)

    print(total(part1(schematic)))

