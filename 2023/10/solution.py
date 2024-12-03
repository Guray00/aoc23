import math


def readfile(filename):
    file = open(filename, "r", encoding="utf-8")

    matrix = []

    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        matrix.append(row)

    file.close()
    return matrix


def east(matrix, i, j):
    return matrix[i][j + 1] if j < len(matrix[i]) - 1 else None


def west(matrix, i, j):
    return matrix[i][j - 1] if j > 0 else None


def south(matrix, i, j):
    return matrix[i + 1][j] if i < len(matrix) else None


def north(matrix, i, j):
    return matrix[i - 1][j] if i > 0 else None


def directions(matrix, i, j):
    pipe = matrix[i][j]

    # 7 - L J S | F
    valid_south = ["L", "|", "J", "S"]
    valid_east = ["-", "J", "7", "S"]
    valid_west = ["-", "L", "F", "S"]
    valid_north = ["7", "|", "F", "S"]

    dnorth, dsouth, dwest, deast = (-1, 0), (1, 0), (0, -1), (0, 1)

    directions = []
    match (pipe):
        case "F":
            if south(matrix, i, j) in valid_south:
                directions.append(dsouth)
            if east(matrix, i, j) in valid_east:
                directions.append(deast)
        case "L":
            if north(matrix, i, j) in valid_north:
                directions.append(dnorth)
            if east(matrix, i, j) in valid_east:
                directions.append(deast)
        case "J":
            if north(matrix, i, j) in valid_north:
                directions.append(dnorth)
            if west(matrix, i, j) in valid_west:
                directions.append(dwest)
        case "-":
            if west(matrix, i, j) in valid_west:
                directions.append(dwest)
            if east(matrix, i, j) in valid_east:
                directions.append(deast)
        case "|":
            if south(matrix, i, j) in valid_south:
                directions.append(dsouth)
            if north(matrix, i, j) in valid_north:
                directions.append(dnorth)
        case "7":
            if south(matrix, i, j) in valid_south:
                directions.append(dsouth)
            if west(matrix, i, j) in valid_west:
                directions.append(dwest)
        case "S":
            if west(matrix, i, j) in valid_west:
                directions.append(dwest)
            if east(matrix, i, j) in valid_east:
                directions.append(deast)
            if north(matrix, i, j) in valid_north:
                directions.append(dnorth)
            if south(matrix, i, j) in valid_south:
                directions.append(dsouth)

    return directions


# def valid_direction(pipe, newpipe, direction):
# match(pipe):
# case 'F':


def find_start(matrix):
    for i, row in enumerate(matrix):
        for j, ceil in enumerate(row):
            if ceil == "S":
                return (i, j)
    return None


"""
// correct, but recursion depth exceeded
def dfs(matrix, i, j, counter=0, prec=None):
    d = directions(matrix, i, j)

    if len(d) < 2: return None
    if prec and prec in d: d.remove(prec)

    for direction in d:
        if matrix[i+direction[0]][j + direction[1]] == 'S':
            return math.ceil(counter/2)

        prec = (direction[0] * -1, direction[1] * -1)
        res = dfs(matrix, i+direction[0], j+direction[1], counter+1, prec)
        if res != None:
            return res

    return -1
"""


def dfs_iterative(matrix, start_i, start_j):
    # stack to calculate all the possible ways
    stack = [(start_i, start_j, [], None)]

    while stack:
        i, j, path, prec = stack.pop()
        d = directions(matrix, i, j)

        if len(d) < 2:
            continue  # no pipe continuing
        if prec and prec in d:
            d.remove(prec)  # removing source pipe as direction

        for direction in d:
            new_i, new_j = i + direction[0], j + direction[1]

            if matrix[new_i][new_j] == "S":  # checking if arrived
                return path

            prec = (direction[0] * -1, direction[1] * -1)
            path.append((new_i, new_j))
            stack.append((new_i, new_j, path, prec))

    return -1


def first_part(matrix):
    i, j = find_start(matrix)
    path = dfs_iterative(matrix, i, j)

    return math.ceil(len(path) / 2)


def change_board(matrix, i, j, path):
    for i, row in enumerate(matrix):
        for j, ceil in enumerate(row):
            if (i, j) not in path:
                matrix[i][j] = "."


def count_board(matrix):
    distance = 0
    for i, row in enumerate(matrix):
        opened = False

        for j, cell in enumerate(row):
            if opened and cell == ".":
                distance += 1

            match cell:
                case "F":
                    if not opened:
                        opened = cell
                    elif opened == "F" or opened == "|" or opened == "7":
                        opened = False

                case "|":
                    if not opened:
                        opened = cell
                    elif opened == "|" or opened == "7":
                        opened = False

                case "7":
                    if not opened:
                        opened = cell
                    elif opened == "F" or opened == "|":
                        opened = False
                # case 'J':
                # if opened == 'F': opened = False

        print(opened)

    return distance


def print_board(matrix):
    for row in matrix:
        for ceil in row:
            print(ceil, end="")
        print()


def second_part(matrix):
    i, j = find_start(matrix)
    path = dfs_iterative(matrix, i, j)

    # DEVO SOSTITUIRE LA S
    start_dir = directions(matrix, i, j)

    if (1, 0) in start_dir and (1, 0) in start_dir:
        matrix[i][j] = "F"

    # change_board(matrix, i, j, path)
    print_board(matrix)

    return count_board(matrix)


matrix = readfile(r"C:\Users\marco\Workspace\adventofcode23\10\input.txt")
print(first_part(matrix))
print(second_part(matrix))
