import re
from aoc2023.utils import read_txt_file
from collections import defaultdict
from pprint import pprint


def find_wins(card):
    winning_number = set(re.findall(r"\d+", card.split(":")[1].split("|")[0]))
    my_picks = set(re.findall(r"\d+", card.split(":")[1].split("|")[1]))
    matches = len(winning_number & my_picks)

    return matches


def part_1(cards):
    total_points = 0
    for card in cards:
        card_point = 0
        matches = find_wins(card)
        if matches > 0:
            card_point += 2 ** (matches - 1)
            total_points += card_point

    return total_points


def part_2(cards):
    result = defaultdict(int)  # old school googling, this is new to me
    for idx, card in enumerate(cards):
        result[idx] += 1
        # card_number = int(re.findall(r"\d+", card.split(":")[0])[0])
        matches = find_wins(card)
        if matches > 0:
            for x in range(matches):
                result[idx + x + 1] += result[idx]

    return sum(result.values())


if __name__ == "__main__":
    cards = read_txt_file("4_puzzle_input.txt")

    print(part_1(cards))
    print(part_2(cards))
