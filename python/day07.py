#!/usr/bin/env python3

import operator as op
import re
from collections.abc import Callable, Iterable
from functools import reduce
from itertools import product

from puzzle_input_getter import get_puzzle_input


class NextOp:
    """Class that returns the next operator when called"""

    def __init__(self, operators: Iterable[Callable[[int, int], int]]):
        self.it = iter(operators)

    def __call__(self, x, y):
        op = next(self.it)
        return op(x, y)


def solve(equations: list[list[int]], operators: Iterable[Callable[[int, int], int]]) -> int:
    total = 0
    for equation in equations:
        result = equation[0]
        operands = equation[1:]

        operators_p = product(operators, repeat=len(operands) - 1)

        for opers in operators_p:
            if result == reduce(NextOp(opers), operands):
                total += result
                break

    return total


def combine(lhs: int, rhs: int) -> int:
    """Append the rhs to the lhs"""
    ndigits = len(str(rhs))

    return lhs * 10**ndigits + rhs


def part1(equations) -> int:
    operators = (op.add, op.mul)

    return solve(equations, operators)


def part2(equations) -> int:
    operators = (op.add, op.mul, combine)

    return solve(equations, operators)


def main() -> None:
    input = get_puzzle_input(year=2024, day=7).splitlines()

    equations = [[int(x) for x in re.findall(r"\d+", line)] for line in input if line]

    print(f"part1: {part1(equations)}")
    print(f"part2: {part2(equations)}")


if __name__ == "__main__":
    main()
