"""Solves day 01, Advent of Code 2023."""

from aocd.models import Puzzle

def first_digit(line: str) -> int:
    "Return the first digit found in a line."
    return next(int(x) for x in line if x.isnumeric())

def last_digit(line: str) -> int:
    "Return the last digit found in a line."
    return next(int(x) for x in reversed(line) if x.isnumeric())

def calibration_value(line: str):
    "Return the calibration value found in a line"
    return first_digit(line) * 10 + last_digit(line)

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    return sum(calibration_value(line) for line in input_data.split())
    

def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    input_data = input_data.replace('one','one1one')
    input_data = input_data.replace('two','two2two')
    input_data = input_data.replace('three','three3three')
    input_data = input_data.replace('four','four4four')
    input_data = input_data.replace('five','five5five')
    input_data = input_data.replace('six','six6six')
    input_data = input_data.replace('seven','seven7seven')
    input_data = input_data.replace('eight','eight8eight')
    input_data = input_data.replace('nine','nine9nine')
    return sum(calibration_value(line) for line in input_data.split())


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=1)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
