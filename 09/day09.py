"""Solves day 09, Advent of Code 2023."""

from aocd.models import Puzzle
import numpy as np

def predict_a(sequence: list[int]) -> int:
    """Predict the next element in the sequence according to Part One's specifications."""
    # list of derived sequences
    seqlist = [np.array(sequence)]
    # while the last derived sequence is not all zeros,
    while any(seqlist[-1]):
        # append a new derived sequence made of the last one's differences
        last_seq = seqlist[-1]
        diffs = last_seq[1:] - last_seq[:-1]
        seqlist.append(diffs)
    # sum the last elements of each derived sequence to obtain the prediction
    return sum(s[-1] for s in seqlist)


def parse_input(input_data: str) -> list[list[int]]:
    """Parse input data, returning a list of lists of ints."""
    lines = input_data.splitlines()
    return [[int(x) for x in line.split()] for line in lines]


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""
    seqs = parse_input(input_data)
    return sum(predict_a(seq) for seq in seqs)


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=9)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
