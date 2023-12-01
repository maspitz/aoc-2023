"""Tests for day 01 of Advent of Code 2023."""

import day01

# Test data given as a multiline string.
sample_input_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

sample_input_data_b = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

sample_solution_a = 142

sample_solution_b = 281


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day01.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day01.part_b(sample_input_data_b) == sample_solution_b
