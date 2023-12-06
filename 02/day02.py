"""Solves day 02, Advent of Code 2023."""

from aocd.models import Puzzle
from parse import parse
from math import prod


def parse_result(result: str) -> dict:
    """Return a dict representing a draw result.
    Example:
    parse_result("3 blue, 4 red") ==
    {'blue': 3, 'red': 4}"""
    parsed_draws = [parse("{:d} {}", x) for x in result.split(", ")]
    return {color: num for (num, color) in parsed_draws}


def parse_line(line: str) -> tuple:
    """Parse the line for a game, returning game number and draw results as a list of dicts."""
    game_str, result_str = line.split(': ')
    game_num = parse("Game {:d}", game_str)
    results = result_str.split('; ')
    return game_num[0], [parse_result(x) for x in results]

def result_is_possible(cubes_drawn: dict, cubes_avail: dict) -> bool:
    """Determine if a result is possible.
    cubes_drawn and cubes_avail are both dicts mapping strings to integers
    to represent the numbers of cubes of each color."""
    return all(cubes_drawn.get(color,0) <= cubes_avail.get(color,0) for color in cubes_drawn.keys())

def game_is_possible(draw_results: list, cubes_avail: dict) -> bool:
    return all(result_is_possible(result, cubes_avail) for result in draw_results)

def min_cubes_needed(draw_results: list) -> tuple:
    colors = set.union(*[set(draw.keys()) for draw in draw_results])
    return tuple(max(draw.get(color,0) for draw in draw_results) for color in colors)

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""
    cubes_avail = parse_result("12 red, 13 green, 14 blue")
    game_data = [parse_line(line)
                 for line in input_data.split('\n')]
    valid_games = [num for num, cubes_drawn in game_data if game_is_possible(cubes_drawn, cubes_avail)]
    return sum(valid_games)


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""
    game_data = [parse_line(line)
                 for line in input_data.split('\n')]
    return sum([prod(min_cubes_needed(draw_results)) for _, draw_results in game_data])



if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=2)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
