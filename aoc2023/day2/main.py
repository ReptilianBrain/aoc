import re

from aoc2023.utils import read_txt_file

BASELINE = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_game(games):
    results = []

    for g in games:
        results.append(
            {
                "red": max(
                    [int(x.replace(" red", "")) for x in re.findall(r"(\d+ red)", g)]
                ),
                "green": max(
                    [
                        int(x.replace(" green", ""))
                        for x in re.findall(r"(\d+ green)", g)
                    ]
                ),
                "blue": max(
                    [int(x.replace(" blue", "")) for x in re.findall(r"(\d+ blue)", g)]
                ),
            }
        )

    return results


def puzzle_a(game_results):
    total = 0
    for k, v in enumerate(game_results):
        if (
            v["red"] <= BASELINE["red"]
            and v["green"] <= BASELINE["green"]
            and v["blue"] <= BASELINE["blue"]
        ):
            total += k + 1

    return total


def puzzle_b(game_results):
    total = 0

    for k, v in enumerate(game_results):
        total += v["red"] * v["green"] * v["blue"]

    return total


if __name__ == "__main__":
    games_file = read_txt_file("2_puzzle_input.txt")[1:]
    games_result = parse_game(games_file)

    print(puzzle_a(games_result))
    print(puzzle_b(games_result))
