def parseLine(line):
    id_ = line[5 : line.index(":")]

    groups = line.strip().replace(f"Card {id_}: ", "").split("|")
    winners = [x for x in groups[0].strip().split(" ") if x != ""]
    owned = [x for x in groups[1].strip().split(" ") if x != ""]

    result = 0

    for n in owned:
        if n in winners:
            result = result * 2 if result > 0 else 1

    return result


def solve(filename):
    file = open(filename, "r", encoding="utf-8")

    total = 0
    for line in file:
        total += parseLine(line)

    file.close()
    return total


print(solve("input.txt"))
