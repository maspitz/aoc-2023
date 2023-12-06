"""Solves day 03, Advent of Code 2023."""

from aocd.models import Puzzle

from collections import namedtuple

import re

Part = namedtuple('Part', ['start', 'end', 'linenum', 'partnum'])

def parse_input_data(input_data: str) -> list:
    return input_data.split('\n')

re_number = re.compile('[0-9]+')

re_symbol = re.compile('[^0-9\.]')

def find_parts(lines: list) -> list['Part']:
    """Return list of candidate parts"""
    output = []
    for linenum, line in enumerate(lines):
        iterator = re_number.finditer(line)
        output.extend([Part(m.start(), m.end(), linenum, int(line[m.start():m.end()])) for m in iterator])
    return output

def part_border(p: 'Part', lines: list) -> str:
    """Return the schematic areas adjacent to the part as a string"""
    m = len(lines)
    n = len(lines[0])
    left_idx = max(0, p.start - 1)
    right_idx = min(n, p.end + 1)
    outstr = ""
    if p.linenum != 0:
        outstr += lines[p.linenum - 1][left_idx:right_idx]
    outstr += lines[p.linenum][left_idx:p.start]
    outstr += lines[p.linenum][p.end:right_idx]
    if p.linenum + 1 != m:
        outstr += lines[p.linenum + 1][left_idx:right_idx]
    return outstr

def part_is_valid(p: 'Part', lines: list) -> bool:
    """Tests whether a candidate part is adjacent to a symbol in the schematic"""
    return bool(re_symbol.search(part_border(p, lines)))

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""
    lines = parse_input_data(input_data)
    parts = find_parts(lines)
    valid_parts = [p for p in parts if part_is_valid(p, lines)]
    return sum([p.partnum for p in valid_parts])


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=3)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
