FILENAME = "input.txt"

from copy import deepcopy
from collections import deque


# retrieves the input file and elaborates it
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    puzzle = []
    for line in file:
        test_value, values = line.strip().split(":")

        test_value = int(test_value)
        values = deque([int(x) for x in values.strip().split(" ")])
        puzzle.append(tuple([test_value, values]))

    return puzzle


def run_simulation(test, values, operations):
    alternatives = set([values.popleft()])

    while values:
        n = values.popleft()

        tmp = set()
        for a in alternatives:
            for op in operations:
                result = op(a, n)
                if result <= test:
                    tmp.add(result)

        alternatives = tmp

    if test in alternatives:
        return True
    return False


def solve_part_one(original_puzzle):
    puzzle = deepcopy(original_puzzle)
    operations = [lambda a, b: a + b, lambda a, b: a * b]

    tot = 0
    for test, values in puzzle:
        alternatives = set([values[0]])

        if run_simulation(test, values, operations):
            tot += test

    return tot


# *************************************
#              part 2
# *************************************


def solve_part_two(original_puzzle):
    puzzle = deepcopy(original_puzzle)
    operations = [
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: a * pow(10, len(str(b))) + b,
    ]

    tot = 0
    for test, values in puzzle:
        alternatives = set([values[0]])

        if run_simulation(test, values, operations):
            tot += test

    return tot


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve_part_one(puzzle)
    print(f"result1: {result1}")

    result2 = solve_part_two(puzzle)
    print(f"result2: {result2}")
