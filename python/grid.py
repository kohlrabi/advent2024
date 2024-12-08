from collections.abc import Iterator
from itertools import product
from typing import Any, no_type_check


class Grid[T]:
    def __init__(self, grid: list[list[T]]) -> None:
        self.grid: list[list[T]] = grid
        self.x_size = len(grid)
        self.y_size = len(grid[0])
        self.dims = (self.x_size, self.y_size)
        self.size = self.x_size * self.y_size

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Grid):
            return NotImplemented
        print(self.grid, other.grid)
        return self.grid == other.grid

    def __iter__(self):
        yield from (col for row in self.grid for col in row)

    def unique(self) -> set[T]:
        return set(iter(self))

    def filled(self, fillvalue: Any) -> "Grid[Any]":
        def make_row():
            return [fillvalue] * self.x_size

        return Grid([make_row() for i in range(self.y_size)])

    def finditer(self, *values: T) -> Iterator[tuple[int, int]]:
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if col in values:
                    yield (i, j)

    @no_type_check
    def finditer_any(self, *values: T) -> Iterator[tuple[int, int]]:
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                for cval in col:
                    if cval in values:
                        yield (i, j)
                    break

    def find(self, *values: T) -> tuple[int, int] | None:
        try:
            return next(self.finditer(*values))
        except StopIteration:
            return None

    def findall(self, *values: T) -> tuple[tuple[int, int], ...]:
        return tuple(self.finditer(*values))

    def count(self, *values: T) -> int:
        return len(self.findall(*values))

    def __getitem__(self, key: tuple[int, int]) -> T:
        x, y = key
        if x < 0 or y < 0:
            raise IndexError("Out of bounds)")
        return self.grid[x][y]

    def __setitem__(self, key: tuple[int, int], value: T) -> None:
        x, y = key
        if x < 0 or y < 0:
            raise IndexError("Out of bounds)")
        self.grid[x][y] = value

    def reverse_x(self) -> "Grid[T]":
        return Grid([list(reversed(row)) for row in self.grid])

    def reverse_y(self) -> "Grid[T]":
        return Grid([list(row) for row in zip(*reversed([col for col in zip(*self.grid)]))])

    def transpose(self) -> "Grid[T]":
        return Grid(list(list(x) for x in zip(*self.grid)))

    def match_pattern(self, pattern: "Grid[T]|Grid[T|None]", x: int, y: int, ignore: Any = None) -> bool:
        return all(
            self[x + i, y + j] == pattern[i, j] or pattern[i, j] == ignore
            for i, j in product(range(pattern.x_size), range(pattern.y_size))
        )

    def count_matches(self, pattern: "Grid[T]|Grid[T|None]", ignore: Any = None):
        return sum(
            self.match_pattern(pattern, i, j, ignore=ignore)
            for i, j in product(range(self.x_size - pattern.x_size + 1), range(self.y_size - pattern.y_size + 1))
        )

    def copy(self) -> "Grid[T]":
        return Grid([row[:] for row in self.grid])

    def __str__(self) -> str:
        return str(self.grid)
