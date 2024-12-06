#!/usr/bin/env python3


from grid import Grid
from puzzle_input_getter import get_puzzle_input


def part1(array: Grid[str]) -> int:
    pattern = Grid([["X", "M", "A", "S"]])
    pattern_x = Grid(
        [["X", None, None, None], [None, "M", None, None], [None, None, "A", None], [None, None, None, "S"]]
    )

    patterns = (
        pattern,
        pattern.reverse_x(),
        pattern.transpose(),
        pattern.reverse_x().transpose(),
        pattern_x,
        pattern_x.reverse_x(),
        pattern_x.reverse_x().transpose(),
        pattern_x.reverse_x().transpose().reverse_x(),
    )

    return sum(array.count_matches(pattern=pattern) for pattern in patterns)


def part2(array: Grid[str]) -> int:
    pattern = Grid([["M", None, "S"], [None, "A", None], ["M", None, "S"]])

    patterns = (pattern, pattern.reverse_x(), pattern.transpose(), pattern.reverse_x().transpose())

    return sum(array.count_matches(pattern=pattern) for pattern in patterns)


def main() -> None:
    input = get_puzzle_input(year=2024, day=4)

    array = Grid([[x for x in line] for line in input.splitlines()])

    print(f"part1: {part1(array)}")

    print(f"part2: {part2(array)}")


if __name__ == "__main__":
    main()
