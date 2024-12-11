FILENAME = "input.txt"

from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Puzzle:
    matrix: list
    starts: list


# retrieves the input file and elaborates it
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    matrix = []
    starts = []
    for i, line in enumerate(file):
        row = [int(x) for x in list(line.strip())]
        matrix.append(row)

        for j, cell in enumerate(row):
            if cell == 0:
                starts.append(tuple([i, j]))

    return Puzzle(matrix, starts)


def is_valid_position(pos, matrix):
    if 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0]):
        return True


def get_paths(position, matrix):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    values = []
    for d in directions:
        new_position = tuple([position[0] + d[0], position[1] + d[1]])

        if not is_valid_position(new_position, matrix):
            continue

        new_value = get_value(new_position, matrix)
        old_value = get_value(position, matrix)

        if new_value == old_value + 1:
            values.append(new_position)

    return values


def get_value(position, matrix):
    return matrix[position[0]][position[1]]


# not adopted
def set_value(value, position, matrix):
    matrix[position[0]][position[1]] = value


def run_simulation(position, matrix):
    value = get_value(position, matrix)

    # base case
    if value == 9:
        return [position], 1

    finals = set()
    alternatives = get_paths(position, matrix)

    trails = 0
    for alternative in alternatives:
        res, t = run_simulation(alternative, matrix)
        finals.update(res)
        trails += t

    return finals, trails


def solve_part_one(puzzle):
    tot = 0
    for start in puzzle.starts:
        res, _ = run_simulation(start, puzzle.matrix)
        tot += len(res)

    return tot


# *************************************
#              part 2
# *************************************


def solve_part_two(puzzle):
    tot = 0
    for start in puzzle.starts:
        _, res = run_simulation(start, puzzle.matrix)
        tot += res

    return tot


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve_part_one(deepcopy(puzzle))
    print(f"result1: {result1}")

    result2 = solve_part_two(deepcopy(puzzle))
    print(f"result2: {result2}")
