#!/usr/bin/env python3

from collections.abc import Iterator
from itertools import product
from typing import Any

from puzzle_input_getter import get_puzzle_input


def part1(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    return 0


def part2(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    return 0


def main() -> None:
    input = get_puzzle_input(year=2024, day=5)

    rules: list[tuple[int, int]] = []
    updates: list[list[int]] = []

    do_ordering = True
    for line in input.splitlines():
        if not line:
            do_ordering = False
            continue
        if do_ordering:
            ls = line.split("|")
            rules.append((int(ls[0]), int(ls[1])))
        else:
            updates.append([int(x) for x in line.split(",")])

    print(f"part1: {part1(rules, updates)}")

    print(f"part2: {part2(rules, updates)}")


if __name__ == "__main__":
    main()
