#!/usr/bin/env python3

from collections import Counter
from collections.abc import Iterable
from copy import deepcopy
from dataclasses import dataclass

from puzzle_input_getter import get_puzzle_input


@dataclass(slots=True)
class Entry:
    id: int | None
    length: int


def part1(filesystem: list[Entry]) -> int:
    index = 1
    while filesystem[-2].id is None or filesystem[-1].id is None:
        tail = filesystem[-1]
        if tail.id is None:
            filesystem.pop()
            continue

        current = filesystem[index]
        if current.length < tail.length:
            current.id = tail.id
            tail.length -= current.length
            index += 2
        else:
            remainder = current.length - tail.length
            current.length = tail.length
            current.id = tail.id
            filesystem.insert(index + 1, Entry(None, remainder))
            filesystem.pop()
            index += 1

    pos = 0
    total = 0
    for entry in filesystem:
        total += entry.id * sum(range(0 + pos, entry.length + pos))
        pos += entry.length
    return total


def part2(filesystem: list[Entry]) -> int:
    i = len(filesystem) - 1
    moved = set()
    while i > 0:
        # for i in range(-1, -len(filesystem) - 1):
        current = filesystem[i]
        if current.id is None or current.id in moved:
            i -= 1
            continue

        moved.add(current.id)

        for j, entry in enumerate(filesystem):
            if j >= i:
                break
            if entry.id is None and current.id and entry.length >= current.length:
                remainder = entry.length - current.length
                entry.id = current.id
                entry.length = current.length
                current.id = None
                if remainder:
                    filesystem.insert(j + 1, Entry(None, remainder))
                    i += 1
                break

        i -= 1

    pos = 0
    total = 0
    for entry in filesystem:
        if entry.id is None:
            pos += entry.length
            continue
        total += entry.id * sum(range(0 + pos, entry.length + pos))
        pos += entry.length
    return total


def main() -> None:
    input = map(int, get_puzzle_input(year=2024, day=9).splitlines()[0])

    filesystem: list[Entry] = []
    file = True
    id = 0
    for entry in input:
        if file:
            filesystem.append(Entry(id, entry))
            id += 1
            file = False
        else:
            filesystem.append(Entry(None, entry))
            file = True

    print(f"part1: {part1(deepcopy(filesystem))}")
    print(f"part2: {part2(deepcopy(filesystem))}")


if __name__ == "__main__":
    main()
