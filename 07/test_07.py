"""Tests for day 07 of Advent of Code 2023."""

import day07

# Test data given as a multiline string.
sample_input_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

sample_solution_a = 6440

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day07.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day07.part_b(sample_input_data) == sample_solution_b
