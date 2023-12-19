"""Tests for day 08 of Advent of Code 2023."""

import day08

# Test data given as a multiline string.
sample_input_data_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

sample_solution_a_1 = 2

sample_input_data_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

sample_solution_a_2 = 6

sample_input_data_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

sample_solution_b = 6


def test_part_a():
    """Test the solution on sample data for part A."""
    assert day08.part_a(sample_input_data_1) == sample_solution_a_1
    assert day08.part_a(sample_input_data_2) == sample_solution_a_2


def test_part_b():
    """Test the solution on sample data for part B."""
    assert day08.part_b(sample_input_data_3) == sample_solution_b
