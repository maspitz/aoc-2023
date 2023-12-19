"""Solves day 08, Advent of Code 2023."""

from aocd.models import Puzzle
from parse import parse



def parse_input(input_data: str) -> tuple[str, dict]:
    lines = input_data.splitlines()
    instructions = lines[0]
    network_lines = [parse("{} = ({}, {})", line).fixed for line in lines[2:]]

    network = {node: (left, right)
               for node, left, right in network_lines}
    return instructions, network


def apply_steps(location: str, target: str, instructions: str, network: dict) -> tuple[int, str]:
    """Return the number of steps taken and the destination reached in those
    steps according to the given arguments.

    The number of steps will be equal to either the steps until the target is reached,
    or the number of instructions, whichever is smaller."""

    steps = 0
    for direction in instructions:
        if location == target:
            return (steps, location)
        steps += 1
        if direction == 'L':
            location = network[location][0]
        else:
            location = network[location][1]
    return (steps, location)


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    inst, net = parse_input(input_data)
    total_steps = 0
    location = 'AAA'
    target = 'ZZZ'
    while target != location:
        new_steps, location = apply_steps(location, target, inst, net)
        total_steps += new_steps
    return total_steps


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=8)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
