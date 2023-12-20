"""Solves day 08, Advent of Code 2023."""

from aocd.models import Puzzle
from parse import parse
from math import lcm


def parse_input(input_data: str) -> tuple[str, dict]:
    lines = input_data.splitlines()
    instructions = lines[0]
    network_lines = [parse("{} = ({}, {})", line).fixed for line in lines[2:]]

    network = {node: (left, right)
               for node, left, right in network_lines}
    return instructions, network


def apply_steps(location: str, target: str, instructions: str, network: dict) -> tuple[int, str]:
    """Return the number of steps taken and the destination reached in those
    steps according to the given arguments.

    The number of steps will be equal to either the steps until the target is reached,
    or the number of instructions, whichever is smaller."""

    steps = 0
    for direction in instructions:
        if location == target:
            return (steps, location)
        steps += 1
        if direction == 'L':
            location = network[location][0]
        else:
            location = network[location][1]
    return (steps, location)


def part_a(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part A."""

    inst, net = parse_input(input_data)
    total_steps = 0
    location = 'AAA'
    target = 'ZZZ'
    while target != location:
        new_steps, location = apply_steps(location, target, inst, net)
        total_steps += new_steps
    return total_steps

def path_list(node: str, instructions: str, network: dict) -> list[str]:
    """Returns a list of locations visited when applying the instructions to the network,
    including initial and final locations."""
    path = [node]
    for direction in instructions:
        if direction == 'L':
            node = network[node][0]
        else:
            node = network[node][1]
        path.append(node)
    return path

def stem_and_cycle(node: str, instructions: str, network: dict) -> tuple[list[str], list[str]]:
    """Returns a representation of the infinite path visited when repeating the
    instructions.  The representation consists of a non-repeated 'stem' path followed
    by a 'cycle' path to be infinitely repeated.

    Note that while the representation is correct, it is not necessarily minimal
    because the cycle detection is done only each time the instruction set has
    been completed.

    In practice, the puzzle input appears to have only one destination in each path, which
    occurs specifically during the cycle."""

    d = dict()
    history = []
    while not node in d:
        history.append(node)
        path = path_list(node, instructions, network)
        d[node] = path
        node = path[-1]
    idx = history.index(node)
    stem = history[:idx]
    cycle = history[idx:]
    path_stem = [item for n in stem for item in d[n][:-1]]
    path_cycle = [item for n in cycle for item in d[n][:-1]]
    return path_stem, path_cycle

def part_b(input_data: str) -> int:
    """Given the puzzle input data, return the solution for part B."""

    inst, net = parse_input(input_data)
    total_steps = 0
    # the starting positions are all nodes that end with 'A'
    locations = [node for node in net.keys() if node[-1] == 'A']
    # the target positions are all nodes that end with 'Z'
    targets = {node for node in net.keys() if node[-1] == 'Z'}
    stems_and_cycles = [stem_and_cycle(start_node, inst, net) for start_node in locations]
    stems, cycles = list(zip(*stems_and_cycles))
    stem_targets = [[node[-1] == 'Z' for node in stem] for stem in stems]
    cycle_targets = [[node[-1] == 'Z' for node in cycle] for cycle in cycles]
    stem_target_count = [stem.count(True) for stem in stem_targets]
    cycle_target_count = [cycle.count(True) for cycle in cycle_targets]
    # Confirm the special properties observed in the puzzle input:
    # - each stem region contains no target nodes
    if any(x > 0 for x in stem_target_count):
        raise Exception("Target found in stem region")
    # - each cycle region contains a target node
    if any(x == 0 for x in cycle_target_count):
        raise Exception("Target not found in cycle region")
    # - no cycle region contains more than one target node
    if any(x > 1 for x in cycle_target_count):
        raise Exception("Multiple targets found in cycle region")
    # - the distance from the target to the end of the cycle equals
    #   the length of the stem region, so each system behaves
    #   identically to a cycle with no stem and a target at the end,
    #   i.e., all systems are synchronized cycles of varying lengths.
    target_indexes = [x.index(True) for x in cycle_targets]
    stem_lengths = [len(stem) for stem in stems]
    cycle_lengths = [len(cycle) for cycle in cycles]
    if any(stem_length + target_index != cycle_length
           for stem_length, target_index, cycle_length in
           zip(stem_lengths, target_indexes, cycle_lengths)):
        raise Exception("Unsynchronized cycle found")

    # Thus, the first time all targets are reached simultaneously
    # is the LCM of all cycle lengths.
    return lcm(*cycle_lengths)


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=8)

    print(f"Puzzle {puzzle.year}-12-{puzzle.day:02d}: {puzzle.title}")
    print(f"  Part A: {part_a(puzzle.input_data)}")
    print(f"  Part B: {part_b(puzzle.input_data)}")
