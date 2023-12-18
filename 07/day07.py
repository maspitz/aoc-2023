"""Solves day 07, Advent of Code 2023."""

from aocd.models import Puzzle
from collections import Counter
from enum import IntEnum

class HandType(IntEnum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

card_order = "AKQJT98765432"

def parse_data(input_data: str) -> list[tuple[str, int]]:
    """Convert input string into a list of hands and bids."""
    data = [lines.split(' ') for lines in input_data.split('\n')]
    return [(hand, int(bid)) for hand, bid in data]

def hand_type(hand: str) -> HandType:
    c = Counter(hand)
    mc = c.most_common()
    if mc[0][1] == 5:
        return HandType.FIVE_OF_A_KIND
    if mc[0][1] == 4:
        return HandType.FOUR_OF_A_KIND
    if mc[0][1] == 3 and mc[1][1] == 2:
        return HandType.FULL_HOUSE
    if mc[0][1] == 3:
        return HandType.THREE_OF_A_KIND
    if mc[0][1] == 2 and mc[1][1] == 2:
        return HandType.TWO_PAIR
    if mc[0][1] == 2:
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD

def card_strength(card: str) -> int:
    return card_order.find(card)

def hand_strength(hand: str) -> tuple[HandType, int, int, int, int, int]:
    return (hand_type(hand),) + tuple(card_strength(card) for card in hand)

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""
    hands_bids = parse_data(input_data)
    hands_bids.sort(key=lambda hb: hand_strength(hb[0]), reverse=True)
    winnings = [rank * hb[1] for rank, hb in enumerate(hands_bids, start=1)]
    return sum(winnings)

def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=7)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
