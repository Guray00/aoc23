FILENAME = "input.txt"


# returns two list each one with a column
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    matrix = []
    for line in file:
        row = list(line.strip())
        matrix.append(row)

    return matrix


def top_check(matrix, row, column, string):
    coordinates = [(0, 0), (-1, 0), (-2, 0), (-3, 0)]
    word = get_word(matrix, row, column, coordinates)
    return int(word == string)


def bottom_check(matrix, row, column, string):
    coordinates = [(0, 0), (1, 0), (2, 0), (3, 0)]
    word = get_word(matrix, row, column, coordinates)
    return int(word == string)


def left_check(matrix, row, column, string):
    coordinates = [(0, 0), (0, -1), (0, -2), (0, -3)]
    word = get_word(matrix, row, column, coordinates)
    return int(word == string)


def right_check(matrix, row, column, string):
    coordinates = [(0, 0), (0, 1), (0, 2), (0, 3)]
    word = get_word(matrix, row, column, coordinates)
    return int(word == string)


def diagonal_check(matrix, row, column, string):
    coordinates = [(0, 0), (1, 1), (2, 2), (3, 3)]
    word = get_word(matrix, row, column, coordinates)
    return int(word == string)


def reverse_diagonal_check(matrix, row, column, string):
    coordinates = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    word = get_word(matrix, row, column, coordinates)
    return int(word == string)


def diagonal_bottom_left(matrix, row, column, string):
    coordinates = [(0, 0), (1, -1), (2, -2), (3, -3)]
    word = get_word(matrix, row, column, coordinates)
    return int(word == string)


def diagonal_top_right(matrix, row, column, string):
    coordinates = [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
    word = get_word(matrix, row, column, coordinates)
    return int(word == string)


def get_word(matrix, row, column, coordinates):
    word = ""
    for i, j in coordinates:
        if not (0 <= row + i < len(matrix) and 0 <= column + j < len(matrix[0])):
            return ""
        word += matrix[row + i][column + j]
    return word


def checks(matrix, row, column):
    word = "XMAS"
    t = top_check(matrix, row, column, word)
    b = bottom_check(matrix, row, column, word)
    l = left_check(matrix, row, column, word)
    r = right_check(matrix, row, column, word)
    d = diagonal_check(matrix, row, column, word)
    rd = reverse_diagonal_check(matrix, row, column, word)
    rbl = diagonal_bottom_left(matrix, row, column, word)
    rtr = diagonal_top_right(matrix, row, column, word)
    return t + b + l + r + d + rd + rbl + rtr


def solve_part_one(puzzle):
    total = 0
    for i, _ in enumerate(puzzle):
        for j, _ in enumerate(puzzle):
            if puzzle[i][j] == "X":
                total += checks(puzzle, i, j)

    return total


# *************************************
#              part 2
# *************************************


def xmas_check(matrix, row, column):
    c1 = [(-1, -1), (0, 0), (1, 1)]
    c2 = [(1, -1), (0, 0), (-1, 1)]

    w1 = get_word(matrix, row, column, c1)
    w2 = get_word(matrix, row, column, c2)

    if (w1 == "MAS" or w1[::-1] == "MAS") and (w2 == "MAS" or w2[::-1] == "MAS"):
        return 1
    else:
        return 0


def solve_part_two(reports):
    total = 0
    for i, _ in enumerate(puzzle):
        for j, _ in enumerate(puzzle):
            if puzzle[i][j] == "A":
                total += xmas_check(puzzle, i, j)

    return total


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve_part_one(puzzle)
    print(f"result1: {result1}")

    result2 = solve_part_two(puzzle)
    print(f"result2: {result2}")
