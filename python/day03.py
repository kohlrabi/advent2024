#!/usr/bin/env python3

import itertools
import operator
import re

from puzzle_input_getter import get_puzzle_input

re_mul = re.compile(r"mul\((\d+),(\d+)\)")
re_do = re.compile(r"do\(\)")
re_dont = re.compile(r"don't\(\)")


def part1(input: str) -> int:
    matches = re_mul.finditer(input)
    total = sum(operator.mul(*map(int, match.groups())) for match in matches)
    return total


def part2(input: str) -> int:
    enabled: bool = True

    total: int = 0
    combined_regex = re.compile(
        "|".join(f"({regex.pattern})" for regex in (re_mul, re_do, re_dont))
    )
    while input:
        if match := re.search(combined_regex, input):
            mul, p1, p2, do, dont = match.groups()
            if mul and enabled:
                total += int(p1) * int(p2)
            elif do:
                enabled = True
            elif dont:
                enabled = False
            input = input[match.end() :]
        else:
            break

    return total


def main() -> None:
    input = get_puzzle_input(year=2024, day=3)

    print(f"part1: {part1(input)}")
    print(f"part2: {part2(input)}")


if __name__ == "__main__":
    main()
