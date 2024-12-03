FILENAME = "input.txt"


# returns two list each one with a column
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    for line in file:
        pass


def solve_part_one(puzzle):
    pass


# *************************************
#              part 2
# *************************************


def solve_part_two(reports):
    pass


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve_part_one(puzzle)
    print(f"result1: {result1}")

    result2 = solve_part_two(puzzle)
    print(f"result2: {result2}")
