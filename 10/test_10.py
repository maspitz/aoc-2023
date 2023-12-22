"""Tests for day 10 of Advent of Code 2023."""

import day10

# Test data given as a multiline string.
sample_input_data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

sample_solution_a = 8

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day10.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day10.part_b(sample_input_data) == sample_solution_b
