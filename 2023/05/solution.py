from collections import deque


def first_part(filename):
    file = open(filename, "r", encoding="utf-8")

    # retrives the seeds
    seeds = {int(x): int(x) for x in file.readline()[6:].strip().split(" ")}

    prev = seeds
    map = {}
    for i, line in enumerate(file):
        if "map" in line or line == "\n":
            if map != {}:
                prev = map
            map = {}
            continue

        [destination, source, length] = [int(x) for x in line.strip().split(" ")]

        for x in prev:
            value = prev[x]
            if source <= value < source + length:
                diff = value - source
                map[value] = destination + diff
            elif value not in map:
                map[value] = value

    file.close()
    results = [map[x] for x in map]
    return min(results)


# -------------------------------------------------------------------------------------------


def load_gates(filename):
    file = open(filename, "r", encoding="utf-8")

    # retrives the seeds
    infos = [int(x) for x in file.readline()[6:].strip().split(" ")]

    gate = {}
    for i, x in enumerate(infos):
        if i % 2 != 0:
            continue
        gate[(x, x + infos[i + 1] - 1)] = (x, x + infos[i + 1] - 1)

    gates = [gate]
    gate = {}
    for i, line in enumerate(file):
        if "map" in line or line == "\n":
            if gate != {}:
                gates.append(gate)
            gate = {}
            continue

        [destination, source, length] = [int(x) for x in line.strip().split(" ")]
        gate[(source, source + length - 1)] = (destination, destination + length - 1)

    gates.append(gate)
    file.close()
    return gates


def find_intersections(source, gate, destination):
    intersections = []  # intersections found checking source and gate
    missing = []  # source parts not found in the intersection

    source_start, source_end = source[0], source[1]
    gate_start, gate_end = gate[0], gate[1]

    start = max(source_start, gate_start)
    end = min(source_end, gate_end)

    # checking if there is an intersection
    if start <= end:
        # append of the translation
        mapping = destination[0] - gate[0]
        intersections.append((start + mapping, end + mapping))

    # missing part before gate starts
    if source_start < gate_start:
        missing.append((source_start, min(source_end, gate_start - 1)))

    # missing part after gate ends
    if source_end > gate_end:
        missing.append((max(end + 1, source_start), source_end))

    # print(f"source:{source} gate:{gate} intersections: {intersections} missing: {missing}")
    return intersections, missing


def second_part(filename):
    groups = load_gates(filename)

    # recupero i seed da tradurre al primo step
    to_translate = deque([groups[0][x] for x in groups[0]])

    # per ogni mappa di traduzione
    translation = []
    for i, group in enumerate(groups[1:]):
        translation = set()
        while to_translate:
            # recupero l'elemento da tradurre
            source = to_translate.popleft()
            no_translation = True

            # per ogni gate nel gruppo
            for gate in group:
                intersections, missing = find_intersections(source, gate, group[gate])
                translation.update(intersections)

                # se trovo una traduzione ma con rimanenze
                if len(intersections) > 0:
                    no_translation = False
                    to_translate += missing

            # se non ho trovato nessuna intersezione allora copio nella traduzione
            if no_translation:
                translation.update(missing)

        # ho finito di tradurre tutto, ora da tradurre è l'output della vecchia traduzione
        to_translate = deque(translation)

    return min([x[0] for x in translation])


print(first_part("input.txt"))
print(second_part("input.txt"))
