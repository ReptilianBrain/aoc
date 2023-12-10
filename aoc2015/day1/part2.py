from __future__ import annotations

import argparse
import os.path

import pytest


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    result = 0
    floor = 0
    for idx, direction in enumerate(s):
        if direction == "(":
            floor += 1
        else:
            floor += -1
        if floor == -1:
            result += idx + 1
            break
    return result


INPUT_S = "()())"
EXPECTED = 5


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
