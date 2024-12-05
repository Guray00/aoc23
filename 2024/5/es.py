FILENAME = "input.txt"

from dataclasses import dataclass


@dataclass
class Puzzle:
    rules: dict
    updates: list


# retrieves the input file and elaborates it
def parse_puzzle():
    file = open(FILENAME, "r", encoding="utf-8")

    rules = []
    updates = []
    flag_part = True
    for line in file:
        line = line.strip()

        if line == "":
            flag_part = False
            continue

        if flag_part:
            rules.append([int(x) for x in line.split("|")])
        else:
            updates.append([int(x) for x in line.split(",")])

    rules_map = {}
    for key, value in rules:
        rules_map[key] = rules_map.get(key, []) + [value]

    puzzle = Puzzle(rules_map, updates)
    return puzzle


def is_correct(update: list, rules):
    previous = []
    correct = True
    for num in update:
        rules_num = rules.get(num, [])
        intersection = [value for value in rules_num if value in previous]

        if len(intersection) != 0:
            correct = False
            break

        previous.append(num)

    return correct


def get_middle(lst: list):
    return lst[int(len(lst) / 2)]


def solve_part_one(puzzle: Puzzle):
    middle_values = []
    for update in puzzle.updates:
        if is_correct(update, puzzle.rules):
            middle_values.append(get_middle(update))

    return sum(middle_values)


# *************************************
#              part 2
# *************************************


@dataclass
class Num:
    prev: list
    next: list


def extract_rules(update, rules):
    map = set(update)

    adopted_rules = {}

    for num in rules:
        if num in map:
            filtered = []

            for n in rules[num]:
                if n in map:
                    filtered.append(n)

            adopted_rules[num] = filtered

    for n in update:
        if n not in adopted_rules:
            adopted_rules[n] = []

    return adopted_rules


def order_update(update, rules):
    ordered = []

    filtered_rules = extract_rules(update, rules)

    sorted_update = [
        x[0]
        for x in sorted(filtered_rules.items(), key=lambda x: len(x[1]), reverse=True)
    ]
    return sorted_update


def solve_part_two(reports):
    middle_values = []
    for update in puzzle.updates:
        if not is_correct(update, puzzle.rules):
            sorted_update = order_update(update, puzzle.rules)
            middle_values.append(get_middle(sorted_update))

    return sum(middle_values)


if __name__ == "__main__":
    puzzle = parse_puzzle()

    result1 = solve_part_one(puzzle)
    print(f"result1: {result1}")

    result2 = solve_part_two(puzzle)
    print(f"result2: {result2}")
