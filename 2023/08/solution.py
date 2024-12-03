from math import gcd


def readfile(namefile):
    file = open(namefile, "r", encoding="utf-8")

    indications = [int(x == "R") for x in [*file.readline().strip()]]
    mapping = {}

    file.readline()

    for line in file:
        source, destinations = line.split(" = ")
        source = source.strip()
        left, right = destinations.replace("(", "").replace(")", "").split(",")
        left = left.strip()
        right = right.strip()

        mapping[source] = (left, right)

    file.close()
    return indications, mapping


def first_part(indications, mapping):
    path = []

    current = "AAA"
    index = indications[0]

    while current != "ZZZ":
        x = indications[index]
        path.append(current)
        current = mapping[current][x]
        index = (index + 1) % len(indications)

    return len(path)


def second_part(indications, mapping):
    current = [(x, 0) for x in mapping if x[-1] == "A"]

    index = indications[0]
    values = []

    while current:
        x = indications[index]

        for i in range(len(current)):
            node = mapping[current[i][0]][x]
            current[i] = (node, current[i][1])

            if current[i][0][-1] == "Z" and current[i][1] == 0:
                current[i] = (current[i][0], 1)

            elif current[i][0][-1] == "Z" and current[i][1] != 0:
                values.append(current[i][1])
                current[i] = None

            elif current[i][1] != 0:
                current[i] = (current[i][0], current[i][1] + 1)

        current = [x for x in current if x != None]
        index = (index + 1) % len(indications)

    lcm = 1
    for i in values:
        lcm = lcm * i // gcd(lcm, i)

    return lcm


indications, mapping = readfile("input.txt")
print(first_part(indications, mapping))
print(second_part(indications, mapping))
