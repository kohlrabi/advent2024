#!/usr/bin/env python3

from collections import Counter
from collections.abc import Iterable

from puzzle_input_getter import get_puzzle_input


def part1(first: Iterable[int], second: Iterable[int]) -> int:
    diff = (abs(f - s) for f, s in zip(sorted(first), sorted(second)))
    return sum(diff)


def part2(first: Iterable[int], second: Iterable[int]) -> int:
    second_counts = Counter(second)
    similarity = (f * second_counts[f] for f in first if f in second_counts)
    return sum(similarity)


def main() -> None:
    input = get_puzzle_input(year=2024, day=1).splitlines()
    first, second = tuple(zip(*((int(n) for n in line.split()) for line in input)))
    print(f"part1: {part1(first, second)}")
    print(f"part2: {part2(first, second)}")


if __name__ == "__main__":
    main()
