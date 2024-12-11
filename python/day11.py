#!/usr/bin/env python3

from collections.abc import Sequence
from concurrent.futures import ProcessPoolExecutor
from itertools import chain

from puzzle_input_getter import get_puzzle_input


def evolve(stones: Sequence[int]):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif (ls := len(ss := str(stone))) % 2 == 0:
            new_stones.append(int(ss[: ls // 2], 10))
            new_stones.append(int(ss[ls // 2 :], 10))
        else:
            new_stones.append(stone * 2024)
    return new_stones


def evolve_one(stone: int):
    if stone == 0:
        return [1]
    elif (ls := len(ss := str(stone))) % 2 == 0:
        return [int(ss[: ls // 2], 10), (int(ss[ls // 2 :], 10))]
    else:
        return [stone * 2024]


def evolve_multi(stones: Sequence[int]):
    with ProcessPoolExecutor() as pool:
        new_stones = list(chain.from_iterable(pool.map(evolve_one, stones, chunksize=1000)))
    return new_stones


def part1(stones: Sequence[int]) -> int:
    for _ in range(25):
        stones = evolve_multi(stones)
    return len(stones)


def part2(stones: Sequence[int]) -> int:
    for _ in range(75):
        print(_)
        stones = evolve_multi(stones)
    return len(stones)


def main() -> None:
    input = get_puzzle_input(year=2024, day=11).splitlines()[0]
    stones = [int(x) for x in input.split()]

    print(f"part1: {part1(stones[:])}")
    print(f"part2: {part2(stones[:])}")


if __name__ == "__main__":
    main()
