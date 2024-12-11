FILENAME = "input.txt"


# returns two list each one with a column
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    column1 = []
    column2 = []

    for line in file:
        # I inserted the first value in c1 and the second one in c2
        [c1, c2] = line.strip().split("   ")
        column1.append(int(c1))
        column2.append(int(c2))

    # returns the columns
    return column1, column2


def solve_part_one():
    c1, c2 = parse_puzzle()

    c1.sort()
    c2.sort()
    tot = 0

    for i, el in enumerate(c1):
        tot += abs(c1[i] - c2[i])

    return tot


def sum_of_products(d):
    tot = 0
    for k in d:
        tot += k * d[k]

    return tot


def solve_part_two():
    c1, c2 = parse_puzzle()
    d = {}

    for x in c1:
        d[x] = 0

    for x in c2:
        if x in d:
            d[x] += 1

    return sum_of_products(d)


if __name__ == "__main__":
    result1 = solve_part_one()
    print(f"result1: {result1}")

    result2 = solve_part_two()
    print(f"result2: {result2}")
