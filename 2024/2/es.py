FILENAME = "input.txt"

# returns two list each one with a column
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    levels = []
    for line in file:
        levels.append([int(x) for x in line.strip().split(" ")])

    return levels

def analyze_level(level):
    asc = level[0] < level[1]

    for i,x in enumerate(level[0:-1]):
        diff = level[i+1] - level[i]

        if asc and not 1<=diff<=3:
            return False

        elif not asc and not -3<=diff<=-1:
            return False

    return True


def solve_part_one(levels):
    counter = 0
    for level in levels:
        counter += 1 if analyze_level(level) else 0

    return counter

# *************************************
#              part 2
# *************************************

def verify_report(report)->bool:
    diffs = []

    for i,_ in enumerate(report[0:-1]):
        diff = report[i+1] - report[i]
        diffs.append(diff)

    prec = report[1] - report[0]
    for i,x in enumerate(diffs):
        if not 1<=abs(x)<=3:
            return False, i
        elif x == 0:
            return False, i
        elif prec * x < 0: # different signs in case
            return False, i
        prec = x
    
    return True, None


def solve_part_two(reports):
    counter = 0
    for report in reports:
        result, error_index = verify_report(report)

        if not result:
            combination1 = report[0:error_index] + report[error_index+1:]
            combination2 = report[0:error_index-1] + report[error_index:]
            combination3 = report[0:error_index+1] + report[min(error_index+2, len(report)):]
            counter += int(verify_report(combination1)[0] or verify_report(combination2)[0] or verify_report(combination3)[0])

        else:
            counter += 1

    return counter


if __name__ == "__main__":
    levels = parse_puzzle()

    result1 = solve_part_one(levels)
    print(f"result1: {result1}")

    result2 = solve_part_two(levels)
    print(f"result2: {result2}")
