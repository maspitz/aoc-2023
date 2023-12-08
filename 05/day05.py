"""Solves day 05, Advent of Code 2023."""

from aocd.models import Puzzle

from parse import parse

from dataclasses import dataclass
from collections import namedtuple

PlantData = namedtuple('PlantData', ['category', 'value'])

@dataclass
class PlantDataMap:
    """Class to transform plant data from a source category to a destination category."""
    source_category: str
    dest_category: str
    rules: list

    def transform(self, data: PlantData) -> PlantData:
        if data.category != self.source_category:
            raise Exception(f"{self.source_category}->{self.dest_category} rule"
                            f" cannot be applied to {data}")
        val = data.value
        for dst_start, src_start, range_len in self.rules:
            if src_start <= val and val < src_start + range_len:
                return PlantData(self.dest_category, val + dst_start - src_start)
        return PlantData(self.dest_category, val)


def map_from_specification(map_spec: str) -> PlantDataMap:
    """Parse map specification to build and return the corresponding PlantDataMap"""
    lines = map_spec.split('\n')
    src_cat, dst_cat = parse("{}-to-{} map:", lines[0])
    rules = [[int(x) for x in line.split()] for line in lines[1:]]
    return PlantDataMap(src_cat, dst_cat, rules)

def parse_input_data(input_data: str) -> tuple:
    """Returns a list of seed numbers and a list of map specifications"""
    seeds_str, *map_strs = input_data.split('\n\n')
    seed_nums = parse("seeds: {}", seeds_str)[0]
    seeds = [int(seed) for seed in seed_nums.split()]
    return seeds, map_strs

def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""
    seeds, map_specs = parse_input_data(input_data)
    data_maps = [map_from_specification(s) for s in map_specs]
    data = [PlantData('seed', i) for i in seeds]
    for dm in data_maps:
        data = [dm.transform(d) for d in data]
    locations = [d.value for d in data]
    return min(locations)


def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    return "Solution not implemented"


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=5)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
