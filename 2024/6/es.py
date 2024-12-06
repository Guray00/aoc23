FILENAME = "input.txt"

from dataclasses import dataclass
from enum import Enum
from copy import deepcopy, copy


class Directions(Enum):
    NORTH = [-1, 0]
    EAST = [0, 1]
    SOUTH = [1, 0]
    WEST = [0, -1]


def rotate(d):
    sequence = list(Directions)
    i = sequence.index(d)
    return sequence[(i + 1) % len(sequence)]


@dataclass
class Puzzle:
    position: list
    matrix: list
    direction: Directions


# retrieves the input file and elaborates it
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    puzzle = Puzzle([], [], Directions.NORTH)
    for i, line in enumerate(file):
        row = list(line.strip())
        if "^" in row:
            puzzle.position = [i, row.index("^")]
        puzzle.matrix.append(row)

    return puzzle


def set_matrix_cell(matrix, position, value):
    matrix[position[0]][position[1]] = value


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def is_on_corner(puzzle):
    matrix = puzzle.matrix
    position = puzzle.position
    direction = puzzle.direction

    if direction == Directions.NORTH and position[0] == 0:
        return True
    elif direction == Directions.SOUTH and position[0] == len(matrix) - 1:
        return True
    elif direction == Directions.EAST and position[1] == len(matrix[0]) - 1:
        return True
    elif direction == Directions.WEST and position[1] == 0:
        return True

    return False


def check_valid_position(p, length):
    return 0 <= p < length


def move(puzzle):
    new_position = [
        puzzle.position[0] + puzzle.direction.value[0],
        puzzle.position[1] + puzzle.direction.value[1],
    ]

    while (
        check_valid_position(new_position[0], len(puzzle.matrix))
        and check_valid_position(new_position[1], len(puzzle.matrix[0]))
        and puzzle.matrix[new_position[0]][new_position[1]] != "#"
    ):
        set_matrix_cell(puzzle.matrix, puzzle.position, "X")
        puzzle.position = new_position
        set_matrix_cell(puzzle.matrix, puzzle.position, "^")
        new_position = [
            puzzle.position[0] + puzzle.direction.value[0],
            puzzle.position[1] + puzzle.direction.value[1],
        ]

    # returns the obstacle position
    return tuple([tuple(puzzle.position), puzzle.direction.name])


def count_path(matrix):
    tot = 0
    for row in matrix:
        for cell in row:
            if cell == "X":
                tot += 1
    return tot


def solve_part_one(puzzle):
    starting_position = puzzle.position
    while True:
        move(puzzle)

        if is_on_corner(puzzle):
            set_matrix_cell(puzzle.matrix, puzzle.position, "X")
            break

        puzzle.direction = rotate(puzzle.direction)

    puzzle.position = starting_position
    return count_path(puzzle.matrix)


# *************************************
#              part 2
# *************************************


def run_simulation(original_puzzle, i, j):
    # avoid changes to the original puzzle
    puzzle = deepcopy(original_puzzle)
    stops = set()

    # add the obstacle
    set_matrix_cell(puzzle.matrix, [i, j], "#")

    value = 0
    while True:
        stop = move(puzzle)
        if stop in stops:
            value = 1
            break

        if is_on_corner(puzzle):
            value = 0
            break

        stops.add(stop)
        puzzle.direction = rotate(puzzle.direction)

    return value


def solve_part_two(puzzle):
    # reset the puzzle
    set_matrix_cell(puzzle.matrix, puzzle.position, "^")
    puzzle.direction = Directions.NORTH

    loops = 0
    for i, row in enumerate(puzzle.matrix):
        for j, cell in enumerate(row):
            if cell == "X":
                loops += run_simulation(puzzle, i, j)

    return loops


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve_part_one(puzzle)
    print(f"result1: {result1}")

    result2 = solve_part_two(puzzle)
    print(f"result2: {result2}")
