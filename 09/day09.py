"""Solves day 09, Advent of Code 2023."""

from aocd.models import Puzzle
import numpy as np

def diff_sequences(seq: list[int]) -> list[np.ndarray]:
    """Return successive lists of differences of sequence elements
    up until and including the earliest list of only zeroes."""
    diff_seqlist = [np.array(seq)]
    while any(diff_seqlist[-1]):
        last_seq = diff_seqlist[-1]
        diffs = last_seq[1:] - last_seq[:-1]
        diff_seqlist.append(diffs)
    return diff_seqlist


def predict_a(seq: list[int]) -> int:
    """Predict the next element in the sequence according to Part One's specifications."""
    diff_seq = diff_sequences(seq)
    return sum(ds[-1] for ds in diff_seq)


def predict_b(seq: list[int]) -> int:
    """Predict the next element in the sequence according to Part One's specifications."""
    diff_seq = diff_sequences(seq)
    # Carrying out the prediction by hand shows it is an
    # alternating sum of the first sequence elements.
    return sum(ds[0] * (+1 if (idx % 2 == 0) else -1)
               for idx, ds in enumerate(diff_seq))


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
    seqs = parse_input(input_data)
    return sum(predict_b(seq) for seq in seqs)


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=9)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
