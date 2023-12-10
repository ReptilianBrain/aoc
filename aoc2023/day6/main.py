import math
import re


def part_1(puzzle):
    data = puzzle.splitlines()
    times = [int(x) for x in data[0].split()[1:]]
    distances = [int(x) for x in data[1].split()[1:]]  # safer then using regex ?

    results = []
    for time, distance in zip(times, distances):
        button = 0
        for r in range(time + 1):
            d = r * (time - r)
            if d > distance:
                button += 1
        results.append(button)

    return math.prod(results)


def part_2(puzzle):
    data = puzzle.splitlines()
    time = int("".join(re.findall(r"\d+", data[0])))
    distance = int("".join(re.findall(r"\d+", data[1])))

    for r in range(1, (time - 1)):
        d = r * (time - r)
        if d > distance:
            break
    return time - (2 * r) + 1  # please don't ask


if __name__ == "__main__":
    with open("6_puzzle_input.txt") as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
