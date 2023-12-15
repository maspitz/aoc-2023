"""Tests for day 06 of Advent of Code 2023."""

import day06

# Test data given as a multiline string.
sample_input_data = """Time:      7  15   30
Distance:  9  40  200"""

sample_solution_a = 288

sample_solution_b = 71503


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day06.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day06.part_b(sample_input_data) == sample_solution_b
