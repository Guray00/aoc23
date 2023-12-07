def parseLine(line):
    id_ = line[5:line.index(":")]
    result = {
        "id": int(id_),
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
        
        if values["red"] <= 12 and values["green"] <= 13 and values["blue"] <= 14:
            total += values["id"]
    
    file.close()
    return total
    
    
print(solve("input.txt"))