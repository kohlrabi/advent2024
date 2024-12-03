#!/usr/bin/env python3

import itertools
import operator
from collections.abc import Sequence
from itertools import pairwise

from puzzle_input_getter import get_puzzle_input


def is_sorted(report: Sequence[int]) -> bool:
    """Returns True if report is sorted in increasing OR decreasing order"""
    if len(report) <= 2:
        return True
    op = operator.lt if report[0] < report[1] else operator.gt
    return all(op(x, y) for x, y in pairwise(report))


def is_safe(report: Sequence[int]) -> bool:
    if is_sorted(report):
        return all(1 <= abs(x - y) <= 3 for x, y in pairwise(report))
    return False


def part1(reports: Sequence[Sequence[int]]) -> int:
    total = sum(is_safe(report) for report in reports)
    return total


def part2(reports: Sequence[Sequence[int]]) -> int:
    total = sum(
        any(is_safe(combination) for combination in itertools.combinations(report, len(report) - 1))
        for report in reports
    )
    return total


def main() -> None:
    input = get_puzzle_input(year=2024, day=2).splitlines()
    reports = [[int(x) for x in line.split()] for line in input]
    print(f"part1: {part1(reports)}")
    print(f"part2: {part2(reports)}")


if __name__ == "__main__":
    main()
