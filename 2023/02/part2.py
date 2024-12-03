def power(obj):
    total = 1
    for key in obj:
        if obj[key] != 0:
            total *= obj[key]
    return total


def parseLine(line):
    id_ = line[5 : line.index(":")]
    result = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }

    groups = line.strip().replace(f"Game {id_}: ", "").split(";")

    for group in groups:
        elements = group.split(",")

        for element in elements:
            value = int(element.strip().split(" ")[0])
            color = element.strip().split(" ")[1]

            if result[color] < value:
                result[color] = value

    return result


def solve(filename):
    file = open(filename, "r", encoding="utf-8")
    total = 0
    for line in file:
        values = parseLine(line)
        total += power(values)

    file.close()
    return total


print(solve("input.txt"))
