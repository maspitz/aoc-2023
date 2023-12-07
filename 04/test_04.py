"""Tests for day 04 of Advent of Code 2023."""

import day04

# Test data given as a multiline string.
sample_input_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

sample_solution_a = 13

sample_solution_b = 30


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day04.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day04.part_b(sample_input_data) == sample_solution_b
