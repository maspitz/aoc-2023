"""Tests for day 02 of Advent of Code 2023."""

import day02

# Test data given as a multiline string.
sample_input_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

sample_solution_a = 8

sample_solution_b = 2286


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day02.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day02.part_b(sample_input_data) == sample_solution_b

test_part_a()
