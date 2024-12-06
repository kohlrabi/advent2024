#!/usr/bin/env python3

from collections.abc import Iterator
from itertools import product
from typing import Any

from puzzle_input_getter import get_puzzle_input


class Grid[T]:
    def __init__(self, grid: list[list[T]]) -> None:
        self.grid = grid
        self.x_size = len(grid)
        self.y_size = len(grid[0])
        self.dims = (self.x_size, self.y_size)

    def __getitem__(self, key: tuple[int, int]) -> T:
        x, y = key
        return self.grid[x][y]

    def match_pattern(self, pattern: "Grid[T]", x: int, y: int, ignore: Any = None) -> bool:
        return all(
            self[x + i, y + j] == pattern[i, j] or pattern[i, j] == ignore
            for i, j in product(range(pattern.x_size), range(pattern.y_size))
        )

    def count_matches(self, pattern: "Grid[T]", ignore: Any = None):
        return sum(
            self.match_pattern(pattern, i, j, ignore=ignore)
            for i, j in product(range(self.x_size - pattern.x_size + 1), range(self.y_size - pattern.y_size + 1))
        )

    def __str__(self) -> str:
        return str(self.grid)


def part1(array: Grid[str]) -> int:
    patterns: Iterator[Grid] = (
        Grid(pattern)
        for pattern in (
            [["X", "M", "A", "S"]],
            [["S", "A", "M", "X"]],
            [["X"], ["M"], ["A"], ["S"]],
            [["S"], ["A"], ["M"], ["X"]],
            [["X", None, None, None], [None, "M", None, None], [None, None, "A", None], [None, None, None, "S"]],
            [["S", None, None, None], [None, "A", None, None], [None, None, "M", None], [None, None, None, "X"]],
            [[None, None, None, "X"], [None, None, "M", None], [None, "A", None, None], ["S", None, None, None]],
            [[None, None, None, "S"], [None, None, "A", None], [None, "M", None, None], ["X", None, None, None]],
        )
    )

    return sum(array.count_matches(pattern=pattern) for pattern in patterns)


def part2(array: Grid[str]) -> int:
    patterns: Iterator[Grid] = (
        Grid(pattern)
        for pattern in (
            [["M", None, "S"], [None, "A", None], ["M", None, "S"]],
            [["S", None, "M"], [None, "A", None], ["S", None, "M"]],
            [["M", None, "M"], [None, "A", None], ["S", None, "S"]],
            [["S", None, "S"], [None, "A", None], ["M", None, "M"]],
        )
    )

    return sum(array.count_matches(pattern=pattern) for pattern in patterns)


def main() -> None:
    input = get_puzzle_input(year=2024, day=4)

    array = Grid([[x for x in line] for line in input.splitlines()])

    print(f"part1: {part1(array)}")

    print(f"part2: {part2(array)}")


if __name__ == "__main__":
    main()
