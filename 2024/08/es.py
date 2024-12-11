FILENAME = "input.txt"

from copy import deepcopy
from dataclasses import dataclass
from collections import deque


@dataclass
class Puzzle:
    matrix: list
    map: dict
    antinodes: list


# retrieves the input file and elaborates it
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    matrix = []
    map = {}
    antinodes = []
    for i, line in enumerate(file):
        row = list(line.strip())
        matrix.append(row)
        antinodes.append([0 for x in row])

        for j, cell in enumerate(row):
            if cell == ".":
                continue
            map[cell] = deque(map.get(cell, [])) + deque([tuple([i, j])])

    puzzle = Puzzle(matrix, map, antinodes)
    return puzzle


def position_in_matrix(pos, matrix):
    if 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0]):
        return True
    return False


def set_pos_in_matrix(value, pos, matrix):
    matrix[pos[0]][pos[1]] = value


def add_antinodes(n1, n2, antinodes, keep=False):
    x = n2[0] - n1[0]
    y = n2[1] - n1[1]

    a1 = tuple([n1[0] - x, n1[1] - y])
    a2 = tuple([n2[0] + x, n2[1] + y])

    while position_in_matrix(a1, antinodes) or position_in_matrix(a2, antinodes):
        if position_in_matrix(a1, antinodes):
            set_pos_in_matrix(1, a1, antinodes)

        if position_in_matrix(a2, antinodes):
            set_pos_in_matrix(1, a2, antinodes)

        a1 = tuple([a1[0] - x, a1[1] - y])
        a2 = tuple([a2[0] + x, a2[1] + y])

        if not keep:
            break


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def solve_part_one(puzzle):
    for category in puzzle.map:
        values = puzzle.map[category]

        while values:
            n1 = values.popleft()

            for n2 in values:
                add_antinodes(n1, n2, puzzle.antinodes)

    tot = 0
    for row in puzzle.antinodes:
        tot += sum(row)

    return tot


# *************************************
#              part 2
# *************************************


def solve_part_two(puzzle):
    for category in puzzle.map:
        values = puzzle.map[category]

        while values:
            n1 = values.popleft()

            # now the antennas count as antinodes
            set_pos_in_matrix(1, n1, puzzle.antinodes)

            for n2 in values:
                add_antinodes(n1, n2, puzzle.antinodes, True)

    tot = 0
    for row in puzzle.antinodes:
        tot += sum(row)

    return tot


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve_part_one(deepcopy(puzzle))
    print(f"result1: {result1}")

    result2 = solve_part_two(deepcopy(puzzle))
    print(f"result2: {result2}")
