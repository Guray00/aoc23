FILENAME = "input.txt"

import re


# returns two list each one with a column
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    src = str(file.read()).replace("\n", "").strip()
    file.close()

    operations = [
        (int(x[0]), int(x[1]))
        for x in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", src)
    ]
    return operations


# *************************************
#              part 2
# *************************************


def parse_puzzle_with_do():
    file = open(FILENAME, "r", encoding="utf-8")

    src = str(file.read()).replace("\n", "").strip()
    file.close()

    pattern = r"(do\(\).*?(don\'t\(\)|$))|(^.*?don\'t\(\))"
    regex = re.compile(pattern)
    dos = regex.findall(src)

    do_src = ""
    for do in dos:
        for x in do:
            do_src += x.replace("don't()", "").replace("do()", "")

    operations = [
        (int(x[0]), int(x[1]))
        for x in re.findall(r"mul\(([0-9]{1,3}),[ ]?([0-9]{1,3})\)", do_src)
    ]
    return operations


def solve(puzzle):
    tot = 0

    for x in puzzle:
        tot += x[0] * x[1]

    return tot


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve(puzzle)
    print(f"result1: {result1}")

    puzzle = parse_puzzle_with_do()
    result2 = solve(puzzle)
    print(f"result2: {result2}")
