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


def walk(grid: Grid[str], visited: Grid[int], pos_dir: PosDir) -> PosDir:
    x, y, direction = pos_dir
    visited[x, y] = 1

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
        return ()
    return x, y, direction


def part1(grid: Grid[str]) -> int:
    visited = grid.filled(0)
    if pos := grid.find("^"):
        pos_dir = *pos, "^"
    else:
        raise ValueError("No guard found on map")
    while pos_dir := walk(grid, visited=visited, pos_dir=pos_dir):
        pass
    return visited.count(1)


def part2(array: Grid[str]) -> int:
    return 0


def main() -> None:
    input = get_puzzle_input(year=2024, day=6)

    array = Grid([[x for x in line] for line in input.splitlines()])

    print(f"part1: {part1(array)}")

    print(f"part2: {part2(array)}")


if __name__ == "__main__":
    main()
