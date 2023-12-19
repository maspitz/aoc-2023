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

card_order_joker = "AKQT98765432J"

def parse_data(input_data: str) -> list[tuple[str, int]]:
    """Convert input string into a list of hands and bids."""
    data = [lines.split(' ') for lines in input_data.split('\n')]
    return [(hand, int(bid)) for hand, bid in data]

def hand_type(hand: str) -> HandType:
    c = Counter(hand)
    top_two_count = [count for val, count in c.most_common()[:2]]
    if top_two_count == [5]:
        return HandType.FIVE_OF_A_KIND
    if top_two_count == [4,1]:
        return HandType.FOUR_OF_A_KIND
    if top_two_count == [3,2]:
        return HandType.FULL_HOUSE
    if top_two_count == [3,1]:
        return HandType.THREE_OF_A_KIND
    if top_two_count == [2,2]:
        return HandType.TWO_PAIR
    if top_two_count == [2,1]:
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD

def hand_type_joker(hand: str) -> HandType:
    jokers = hand.count('J')
    if jokers >= 4:
        return HandType.FIVE_OF_A_KIND
    rest_hand = hand.replace('J','')
    c = Counter(rest_hand)
    top_two_count = [count for val, count in c.most_common()[:2]]
    if jokers == 3:
        if top_two_count == [2]:
            return HandType.FIVE_OF_A_KIND
        else:
            return HandType.FOUR_OF_A_KIND
    if jokers == 2:
        if top_two_count == [3]:
            return HandType.FIVE_OF_A_KIND
        elif top_two_count == [2,1]:
            return HandType.FOUR_OF_A_KIND
        else:
            return HandType.THREE_OF_A_KIND
    if jokers == 1:
        if top_two_count == [4]:
            return HandType.FIVE_OF_A_KIND
        elif top_two_count == [3,1]:
            return HandType.FOUR_OF_A_KIND
        elif top_two_count == [2,2]:
            return HandType.FULL_HOUSE
        elif top_two_count == [2,1]:
            return HandType.THREE_OF_A_KIND
        else:
            return HandType.ONE_PAIR
    return hand_type(hand)


def card_strength(card: str) -> int:
    return card_order.find(card)

def card_strength_joker(card: str) -> int:
    return card_order_joker.find(card)

def hand_strength(hand: str) -> tuple[HandType, int, int, int, int, int]:
    return (hand_type(hand),) + tuple(card_strength(card) for card in hand)

def hand_strength_joker(hand: str) -> tuple[HandType, int, int, int, int, int]:
    return (hand_type_joker(hand),) + tuple(card_strength_joker(card) for card in hand)

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""
    hands_bids = parse_data(input_data)
    hands_bids.sort(key=lambda hb: hand_strength(hb[0]), reverse=True)
    winnings = [rank * bid for rank, (hand, bid) in enumerate(hands_bids, start=1)]
    return sum(winnings)

def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""
    hands_bids = parse_data(input_data)
    hands_bids.sort(key=lambda hb: hand_strength_joker(hb[0]), reverse=True)
    winnings = [rank * bid for rank, (hand, bid) in enumerate(hands_bids, start=1)]
    return sum(winnings)


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=7)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
