#!/usr/bin/env python3

from collections import deque

from grid import Grid
from puzzle_input_getter import get_puzzle_input


def walk(array: Grid[int], stack: deque[tuple[int, tuple[int, int]]], count_once: bool = True):
    peaks = set()
    while stack:
        current_value, current_pos = stack.pop()
        if current_value == 9 and current_pos not in peaks:
            if count_once:
                peaks.add(current_pos)
            yield 1
            continue
        for neighbour, neighbour_pos in array.neighbours(current_pos):
            if current_value + 1 == neighbour:
                stack.append((neighbour, neighbour_pos))


def part1(array: Grid[int]) -> int:
    total = 0

    startpositions = array.finditer(0)
    for position in startpositions:
        input = (0, position)
        stack = deque([input])
        total += sum(walk(array, stack, True))

    return total


def part2(array: Grid[str]) -> int:
    total = 0

    startpositions = array.finditer(0)
    for position in startpositions:
        input = (0, position)
        stack = deque([input])
        total += sum(walk(array, stack, False))

    return total


def main() -> None:
    input = get_puzzle_input(year=2024, day=10)

    array = Grid([[int(x) for x in line] for line in input.splitlines()])

    print(f"part1: {part1(array)}")

    print(f"part2: {part2(array)}")


if __name__ == "__main__":
    main()
