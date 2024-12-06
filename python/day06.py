#!/usr/bin/env python3


from grid import Grid
from puzzle_input_getter import get_puzzle_input

PosDir = tuple[int, int, str]

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

directions_keys = list(directions.keys())


class LoopException(Exception):
    pass


def walk(grid: Grid[str], visited: Grid[str], pos_dir: PosDir) -> PosDir:
    x, y, direction = pos_dir

    if direction in visited[x, y]:
        raise LoopException("Found loop in track")
    visited[x, y] += direction

    dx, dy = directions[direction]

    try:
        if grid[x + dx, y + dy] == "#":
            index = directions_keys.index(direction)
            new_direction = directions_keys[(index + 1) % len(directions_keys)]
            direction = new_direction
        else:
            x, y = x + dx, y + dy
    except IndexError:
        # left the map
        raise
    return x, y, direction


def make_visited(grid: Grid[str]) -> Grid[str]:
    visited = grid.filled("")
    if pos := grid.find("^"):
        pos_dir = *pos, "^"
    else:
        raise ValueError("No guard found on map")

    while True:
        try:
            pos_dir = walk(grid, visited=visited, pos_dir=pos_dir)
        except IndexError:
            break
    return visited


def part1(grid: Grid[str]) -> int:
    visited = make_visited(grid)
    return visited.size - visited.count("")


def part2(grid: Grid[str]) -> int:
    if pos := grid.find("^"):
        pos_dir = *pos, "^"
    else:
        raise ValueError("No guard found on map")
    visited = make_visited(grid)

    total = 0
    for vpos in visited.finditer_any(*directions.keys()):
        if pos != vpos:
            new_visited = grid.filled("")
            new_grid = grid.copy()
            new_grid[*vpos] = "#"
            pos_dir = *pos, "^"
            while True:
                try:
                    pos_dir = walk(new_grid, visited=new_visited, pos_dir=pos_dir)
                except IndexError:
                    break
                except LoopException:
                    total += 1
                    break
    return total


def main() -> None:
    input = get_puzzle_input(year=2024, day=6)

    # import pathlib

    # input = pathlib.Path("day06.test").read_text()

    grid = Grid([[x for x in line] for line in input.splitlines()])

    print(f"part1: {part1(grid)}")

    print(f"part2: {part2(grid)}")


if __name__ == "__main__":
    main()
