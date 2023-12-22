"""Solves day 10, Advent of Code 2023."""

from aocd.models import Puzzle
from collections import namedtuple

Coord = namedtuple("Coord", "i,j")

def neighbors(c: Coord) -> list[Coord]:
    """Return the neighbors of a coord."""
    return [Coord(c.i + 1, c.j),
            Coord(c.i - 1, c.j),
            Coord(c.i, c.j + 1),
            Coord(c.i, c.j - 1)]

def connected_coords(c: Coord, grid: list[str]) -> list[Coord]:
    """Return the coords connected to a coord on the grid."""
    m = len(grid)
    n = len(grid[0])
    if (not 0 <= c.i < m) or (not 0 <= c.j < n):
        return []
    tile = grid[c.i][c.j]
    if tile == 'S':
        return [n for n in neighbors(c) if c in connected_coords(n, grid)]
    elif tile == '.':
        return []
    elif tile == '-':
        return [Coord(c.i, c.j - 1), Coord(c.i, c.j + 1)]
    elif tile == '|':
        return [Coord(c.i - 1, c.j), Coord(c.i + 1, c.j)]
    elif tile == 'J':
        return [Coord(c.i, c.j - 1), Coord(c.i - 1, c.j)]
    elif tile == 'F':
        return [Coord(c.i, c.j + 1), Coord(c.i + 1, c.j)]
    elif tile == '7':
        return [Coord(c.i, c.j - 1), Coord(c.i + 1, c.j)]
    elif tile == 'L':
        return [Coord(c.i, c.j + 1), Coord(c.i - 1, c.j)]
    else:
        raise Exception(f"Unknown tile '{tile}' at coord {c}")


def start_coord(grid: list[str]) -> Coord:
    """Return the start coordinate for the grid."""
    for i, row in enumerate(grid):
        j = row.find("S")
        if j != -1:
            return Coord(i,j)
    raise Exception("Start coord not found in grid")


def cycle_length(c: Coord, grid: list[str]) -> int:
    """Follows a cycle and returns its total length."""
    seen = set()
    to_visit = [c]
    length = 0
    while to_visit:
        loc = to_visit.pop()
        if loc in seen:
            continue
        seen.add(loc)
        length += 1
        to_visit.extend(connected_coords(loc, grid))
    return length


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""
    grid = input_data.splitlines()
    sc = start_coord(grid)
    return cycle_length(sc, grid) // 2


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=10)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
