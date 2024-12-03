def loadMatrix(filename):
    file = open(filename, "r", encoding="utf-8")
    matrix = []

    for line in file:
        row = []
        for char in line.strip():
            if char.isdigit():
                row.append(char)
            elif char != ".":
                row.append("#")
            else:
                row.append(".")
        matrix.append(row)

    file.close()
    return matrix


def debugPrint(matrix, y_before, y_after, row, x_start, x_end):
    if y_before != -1:
        print(f"{" ".join(matrix[y_before][x_start:x_end+1])}")
    print(f"{" ".join(matrix[row][x_start:x_end+1])}\t\t\t in row {row}")
    if y_after != -1:
        print(f"{" ".join(matrix[y_after][x_start:x_end+1])}")
    print("")


def check(matrix, row, start, end):
    value = int("".join(matrix[row][start : end + 1]).strip())
    x_start = start - 1 if start > 0 else 0
    x_end = end + 1 if end < len(matrix[row]) - 1 else end

    y_before = row - 1 if row > 0 else -1
    y_after = row + 1 if row < len(matrix) - 1 else -1

    # print(f"{value} {x_start} => {x_end}")
    if matrix[row][x_start] == "#":
        return value
    if matrix[row][x_end] == "#":
        return value

    for x in range(x_start, x_end + 1):
        if y_before != -1 and matrix[y_before][x] == "#":
            return value

        if y_after != -1 and matrix[y_after][x] == "#":
            return value

    # print(f"{value} in line {row}")
    # print(f"{value} {x_start} => {x_end} NO")
    # debugPrint(matrix, y_before, y_after, row, x_start, x_end)
    return 0


def solve(filename):
    matrix = loadMatrix(filename)
    total = 0

    for i, row in enumerate(matrix):
        number = 0
        start = -1

        for j, ceil in enumerate(row):
            # caso in cui trovo un numero
            if ceil.isdigit():
                start = j if start == -1 else start
                number = number * 10 + int(ceil)

            # caso in cui non trovo un numero ma ho già iniziato
            elif start != -1:
                total += check(matrix, i, start, j - 1)
                number = 0
                start = -1

        # se guardo l'ultima cella ma avevo già iniziato
        if matrix[i][len(matrix[i]) - 1].isdigit() and start != -1:
            total += check(matrix, i, start, len(matrix[i]) - 1)
            number = 0
            start = -1

    return total


print(solve(r"C:\Users\marco\Workspace\challenges\adventofcode2023\03\input.txt"))
