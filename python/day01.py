#!/usr/bin/env python3

from collections import Counter
from fileinput import input
from itertools import tee


def part1(input):
    first, second = zip(*((int(n) for n in line.split()) for line in input))
    diff = (abs(f - s) for f, s in zip(sorted(first), sorted(second)))
    return sum(diff)


def part2(input):
    first, second = zip(*((int(n) for n in line.split()) for line in input))
    second_counts = Counter(second)
    similarity = (f * second_counts[f] for f in first if f in second_counts)
    return sum(similarity)


if __name__ == "__main__":
    p1, p2 = tee(input())
    print(f"part1: {part1(p1)}")
    print(f"part2: {part2(p2)}")
