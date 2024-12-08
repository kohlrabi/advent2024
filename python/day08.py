#!/usr/bin/env python3


from itertools import combinations, starmap

from grid import Grid, Vector
from puzzle_input_getter import get_puzzle_input


def find_antinodes(lhs: Vector, rhs: Vector) -> tuple[Vector, Vector]:
    sub = rhs - lhs
    return (
        rhs + sub,
        lhs - sub,
    )


def part1(grid: Grid[str]) -> int:
    visited = grid.filled(0)
    unique = grid.unique()
    unique.remove(".")

    for u in sorted(unique):
        locs = starmap(Vector, grid.findall(u))
        for pair in combinations(locs, 2):
            for antinode in find_antinodes(*pair):
                try:
                    visited[antinode] = 1
                except IndexError:
                    pass

    return visited.count(1)


def part2(grid: Grid[str]) -> int:
    visited = grid.filled(0)
    unique = grid.unique()
    unique.remove(".")

    for u in sorted(unique):
        locs = starmap(Vector, grid.findall(u))
        for pair in combinations(locs, 2):
            sub = pair[1] - pair[0]

            for i in range(1000):
                sub_s = sub * i
                try:
                    visited[pair[1] + sub_s] = 1
                except IndexError:
                    break

            for i in range(1000):
                sub_s = sub * i
                try:
                    visited[pair[0] - sub_s] = 1
                except IndexError:
                    break

    return visited.count(1)


def main() -> None:
    input = get_puzzle_input(year=2024, day=8)

    grid = Grid([[x for x in line] for line in input.splitlines()])

    print(f"part1: {part1(grid)}")

    print(f"part2: {part2(grid)}")


if __name__ == "__main__":
    main()
