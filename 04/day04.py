"""Solves day 04, Advent of Code 2023."""

from aocd.models import Puzzle
from parse import parse

def parse_line(line: str) -> tuple:
    card, win_str, pick_str = parse('{}:{}|{}',line)
    wins = set(int(win) for win in win_str.split())
    picks = set(int(pick) for pick in pick_str.split())
    return (card, wins, picks)

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""
    games = [parse_line(line) for line in input_data.split('\n')]
    matches = [len(set.intersection(wins,picks)) for card, wins, picks in games]
    scores = [0 if x == 0 else pow(2,x-1) for x in matches]
    return sum(scores)


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""
    games = [parse_line(line) for line in input_data.split('\n')]
    matches = [len(set.intersection(wins,picks)) for card, wins, picks in games]
    N = len(games)
    cards = [1] * N
    for i in range(N):
        lo = i + 1
        hi = min(lo + matches[i], N)
        n_copies = cards[i]
        for j in range(lo, hi):
            cards[j] += n_copies
    return sum(cards)


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=4)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
