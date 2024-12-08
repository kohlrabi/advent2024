#!/usr/bin/env python3


from itertools import combinations

from grid import Grid
from puzzle_input_getter import get_puzzle_input

Vector = tuple[int, int]


def sub_vector(lhs: Vector, rhs: Vector) -> Vector:
    return (rhs[0] - lhs[0], rhs[1] - lhs[1])


def find_antinodes(lhs: Vector, rhs: Vector) -> tuple[Vector, Vector]:
    sub = sub_vector(lhs, rhs)
    return (
        (rhs[0] + sub[0], rhs[1] + sub[1]),
        (lhs[0] - sub[0], lhs[1] - sub[1]),
    )


def part1(grid: Grid[str]) -> int:
    visited = grid.filled(0)
    unique = grid.unique()
    unique.remove(".")

    for u in sorted(unique):
        locs = grid.findall(u)
        for pair in combinations(locs, 2):
            for ax, ay in find_antinodes(*pair):
                try:
                    visited[ax, ay] = 1
                except IndexError:
                    pass

    return visited.count(1)


def part2(grid: Grid[str]) -> int:
    return 0


def main() -> None:
    input = get_puzzle_input(year=2024, day=8)

    # import pathlib

    # input = pathlib.Path("day06.test").read_text()

    grid = Grid([[x for x in line] for line in input.splitlines()])

    print(f"part1: {part1(grid)}")

    print(f"part2: {part2(grid)}")


if __name__ == "__main__":
    main()
