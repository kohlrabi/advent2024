#!/usr/bin/env python3

from collections import defaultdict

from puzzle_input_getter import get_puzzle_input


class Rules:
    def __init__(self, rules: list[tuple[int, int]] | None = None) -> None:
        self.rules: dict[int, list[int]] = defaultdict(list)
        if rules is not None:
            for rule in rules:
                self.add_rule(*rule)

    def add_rule(self, first: int, second: int):
        if first not in self.rules:
            self.rules[first] = []
        self.rules[second].append(first)

    def simplify_order(self, update: list[int] | None = None) -> list[tuple[int, list[int]]]:
        if update is None:
            update = []

        rules = []
        for x, y in self.rules.items():
            if x in update:
                lst = []
                for yy in y:
                    if yy in update:
                        lst.append(yy)
                rules.append((x, lst))

        return rules

    def order(self, update: list[int] | None = None) -> list[int]:
        # make a copy of the inner lists to modify them
        rules = self.simplify_order(update)

        ordered: list[int] = []

        rules.sort(key=lambda x: len(x[1]))
        while rules:
            value = rules[0][0]
            rules.pop(0)
            ordered.append(value)

            for _, lst in rules:
                try:
                    lst.remove(value)
                except ValueError:
                    # value not in lst
                    pass
            rules.sort(key=lambda x: len(x[1]))

        return ordered


def part1(rules: Rules, updates: list[list[int]]) -> int:
    total = 0
    for update in updates:
        order = rules.order(update=update)
        update_indices = []
        for entry in update:
            update_indices.append(order.index(entry))
        if sorted(update_indices) == update_indices:
            total += update[len(update) // 2]
    return total


def part2(rules: Rules, updates: list[list[int]]) -> int:
    total = 0
    for update in updates:
        order = rules.order(update=update)
        update_indices = []
        for entry in update:
            update_indices.append(order.index(entry))
        if sorted(update_indices) != update_indices:
            _, sorted_update = zip(*sorted(zip(update_indices, update)))
            total += sorted_update[len(sorted_update) // 2]
    return total


def main() -> None:
    input = get_puzzle_input(year=2024, day=5)

    updates: list[list[int]] = []

    rules = Rules()

    do_ordering = True
    for line in input.splitlines():
        if not line:
            do_ordering = False
            continue
        if do_ordering:
            ls = line.split("|")
            rules.add_rule(int(ls[0]), int(ls[1]))
        else:
            updates.append([int(x) for x in line.split(",")])

    print(f"part1: {part1(rules, updates)}")

    print(f"part2: {part2(rules, updates)}")


if __name__ == "__main__":
    main()
