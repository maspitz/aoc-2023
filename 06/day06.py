"""Solves day 06, Advent of Code 2023."""

from aocd.models import Puzzle
from parse import parse
from math import sqrt, ceil, floor, prod

def parse_input(input_data: str) -> tuple[list[int],list[int]]:
    """Parse the input data, returning a list of times and list of distances."""
    lines = input_data.split('\n')
    ptime = parse("Time:{}",lines[0])
    times = [int(t) for t in ptime[0].split()]
    pdist = parse("Distance:{}",lines[1])
    dists = [int(t) for t in pdist[0].split()]
    return (times, dists)

def ways_to_beat_record(time: int, dist: int) -> int:
    """Return the number of ways to beat a given record distance
    for a race lasting a given time."""

    # v = the speed of our boat.
    # t = time spent holding the button.
    # d = distance boat travels.
    #
    # Then d = v * (time - t)
    # thus  d = t * (time - t).
    #
    # Solve for t:
    # t = (time +/- sqrt(time^2 - 4 * d)) / 2
    #
    # If d = dist, then the record is beaten for all times
    # between the two solutions for t.
    #
    # So: calculate the two solutions and count the integers between them.
    #
    # Note that to beat the record, your boat has to *exceed* the record distance,
    # not just equal it, so if t_plus and t_minus are integers, then the answer
    # is their difference minus one.

    t_plus = (time + sqrt(time * time - 4 * dist)) / 2
    t_minus = (time - sqrt(time * time - 4 * dist)) / 2
    return ceil(t_plus) - floor(t_minus) - 1

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    times, dists = parse_input(input_data)
    ways = [ways_to_beat_record(t, d) for t, d in zip(times, dists)]
    return prod(ways)


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=6)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
