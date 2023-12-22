"""Tests for day 09 of Advent of Code 2023."""

import day09

# Test data given as a multiline string.
sample_input_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

sample_data_predictions_a = [18, 28, 68]

sample_solution_a = 114

sample_solution_b = "Sample solution not entered"


def test_part_a():
    """Test the solution on sample data for part A."""
    lines = sample_input_data.splitlines()
    test_seqs = [[int(x) for x in line.split()] for line in lines]
    for data, pred in zip(test_seqs, sample_data_predictions_a):
        assert day09.predict_a(data) == pred
    assert day09.part_a(sample_input_data) == sample_solution_a


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day09.part_b(sample_input_data) == sample_solution_b
