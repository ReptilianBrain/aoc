import re

from itertools import pairwise


def part_1(puzzle):
    data = puzzle.splitlines()

    sensor_ = [re.findall(r'-?\d+', x) for x in data]
    values = []

    for s in sensor_:
        values.append([int(x) for x in s])

    result = 0
    value_list = []
    for v in values:
        value_list.append(v)

        new_row = [y - x for (x, y) in pairwise(v)]
        value_list.append(new_row)
        while not all(x == 0 for x in new_row):
            new_row = [y - x for (x, y) in pairwise(new_row)]
            value_list.append(new_row)

        for r in range(len(value_list) - 2, -1, -1):  # Does reversed(range) produce similar result ?
            value_list[r].append(value_list[r][-1] + value_list[r+1][-1])

        result += value_list[0][-1]
    return result

def part_2(puzzle):
    data = puzzle.splitlines()

    sensor_ = [re.findall(r'-?\d+', x) for x in data]
    values = []

    for s in sensor_:
        values.append([int(x) for x in s])

    result = 0
    value_list = []
    for v in values:
        print('-----')
        value_list = [v]
        print(value_list[0])
        new_row = [y - x for (x, y) in pairwise(v)]
        print(new_row)
        value_list.append(new_row)
        while not all(x == 0 for x in new_row):
            new_row = [y - x for (x, y) in pairwise(new_row)]
            value_list.append(new_row)
            print(new_row)
        for r in range(len(value_list) - 2, -1, -1):
            value_list[r].insert(0, value_list[r][0] - value_list[r+1][0])

        result += value_list[0][0]
        print(value_list[0][0])
        print('-----')
    return result

if __name__ == "__main__":
    # with open("9_puzzle_input_test.txt") as f:
    with open("9_puzzle_input.txt") as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
