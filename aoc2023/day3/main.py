import re
from typing import NamedTuple
import math
from aoc2023.utils import read_txt_file


class Num(NamedTuple):
    n: int
    y: int
    x: tuple[int, int]

    def adjacent(self, x: int, y: int) -> bool:
        return self.x[0] - 1 <= x < self.x[1] + 1 and self.y - 1 <= y <= self.y + 1


def part1(schematic):
    symbols = set(re.findall(r"[^.|\d]", ".".join([x.rstrip("\n") for x in schematic])))
    valid_value = []
    for idx, _row in enumerate(schematic):
        row = _row.rstrip("\n")

        for n in re.finditer("\\d+", row):
            numb = int(n.group())
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
                for x in schematic[idx + 1][start - 1 : start + end + 1]:
                    if x in symbols:
                        valid_value.append(numb)
            # what's up ?
            if idx != 0:
                for x in schematic[idx - 1][start - 1 : start + end + 1]:
                    if x in symbols:
                        valid_value.append(numb)
    return sum(valid_value)


def part2(schematic):
    # got help here to better learn the concept of working with grid
    total = 0
    gears = []

    for y, line in enumerate(schematic):
        for x, c in enumerate(line):
            if c == "*":
                gears.append((x, y))

    nums = []
    for y, line in enumerate(schematic):
        for match in re.compile(r"\d+").finditer(line):
            nums.append(Num(int(match[0]), y, match.span()))

    for x, y in gears:
        adj = [num for num in nums if num.adjacent(x, y)]
        if len(adj) == 2:
            total += math.prod([adj[0].n, adj[1].n])

    return total


if __name__ == "__main__":
    schematic = read_txt_file("3_puzzle_input.txt")
    # schematic = read_txt_file("3_puzzle_input_test.txt")

    print(part1(schematic))
    print(part2(schematic))
