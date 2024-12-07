#!/usr/bin/env python3

import operator as op
import re
from collections.abc import Callable, Iterable
from functools import reduce
from itertools import product

from puzzle_input_getter import get_puzzle_input


def next_op(operators: Iterable[Callable[[int, int], int]]) -> Callable[[int, int], int]:
    """Return a function that applies the next operator"""
    it = iter(operators)

    def apply_next_op(lhs: int, rhs: int) -> int:
        return next(it)(lhs, rhs)

    return apply_next_op


def solve(equations: list[list[int]], operators: Iterable[Callable[[int, int], int]]) -> int:
    total = 0
    for equation in equations:
        result = equation[0]
        operands = equation[1:]

        operators_p = product(operators, repeat=len(operands) - 1)

        for opers in operators_p:
            if result == reduce(next_op(opers), operands):
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
