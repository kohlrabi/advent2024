#!/usr/bin/env python3

from itertools import product
from typing import Any

from puzzle_input_getter import get_puzzle_input


class Grid[T]:
    def __init__(self, grid: list[list[T]]) -> None:
        self.grid: list[list[T]] = grid
        self.x_size = len(grid)
        self.y_size = len(grid[0])
        self.dims = (self.x_size, self.y_size)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Grid):
            return NotImplemented
        print(self.grid, other.grid)
        return self.grid == other.grid

    def __getitem__(self, key: tuple[int, int]) -> T:
        x, y = key
        return self.grid[x][y]

    def reverse_x(self) -> "Grid[T]":
        return Grid([list(reversed(row)) for row in self.grid])

    def reverse_y(self) -> "Grid[T]":
        return Grid([list(row) for row in zip(*reversed([col for col in zip(*self.grid)]))])

    def transpose(self) -> "Grid[T]":
        return Grid(list(list(x) for x in zip(*self.grid)))

    def match_pattern(self, pattern: "Grid[T]|Grid[T|None]", x: int, y: int, ignore: Any = None) -> bool:
        return all(
            self[x + i, y + j] == pattern[i, j] or pattern[i, j] == ignore
            for i, j in product(range(pattern.x_size), range(pattern.y_size))
        )

    def count_matches(self, pattern: "Grid[T]|Grid[T|None]", ignore: Any = None):
        return sum(
            self.match_pattern(pattern, i, j, ignore=ignore)
            for i, j in product(range(self.x_size - pattern.x_size + 1), range(self.y_size - pattern.y_size + 1))
        )

    def __str__(self) -> str:
        return str(self.grid)


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
