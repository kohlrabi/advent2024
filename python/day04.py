#!/usr/bin/env python3

from collections.abc import Iterator

from puzzle_input_getter import get_puzzle_input


def get_neighbours(array: list[list[str]], row: int, col: int) -> Iterator[tuple[int, int]]:
    rows, cols = len(array), len(array[0])
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (0 <= r < rows) and (0 <= c < cols) and (r != row or c != col):
                yield (r, c)


def part1(array: list[list[str]]) -> int:
    total = 0
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] == "X":
                for r, c in get_neighbours(array, row, col):
                    if array[r][c] == "M":
                        direction = (r - row, c - col)
                        for r2, c2 in get_neighbours(array, r, c):
                            if array[r2][c2] == "A" and direction == (r2 - r, c2 - c):
                                for r3, c3 in get_neighbours(array, r2, c2):
                                    if array[r3][c3] == "S" and direction == (r3 - r2, c3 - c2):
                                        total += 1
    return total


def part2(array: list[list[str]]) -> int:
    return 0


def main() -> None:
    input = get_puzzle_input(year=2024, day=4)

    array = [[x for x in line] for line in input.splitlines()]

    print(f"part1: {part1(array)}")
    print(f"part2: {part2(array)}")


if __name__ == "__main__":
    main()
