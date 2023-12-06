"""Tests for day 03 of Advent of Code 2023."""

import day03

# Test data given as a multiline string.
sample_input_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

sample_solution_a = 4361

sample_solution_b = 467835


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day03.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day03.part_b(sample_input_data) == sample_solution_b
