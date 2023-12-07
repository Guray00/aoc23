from collections import deque

def parseLine(line):
    id_ = int(line[5:line.index(":")])

    groups = line.strip().replace(f"Card {id_}: ", "").split("|")
    winners = [x for x in groups[0].strip().split(" ") if x != ""]
    owned   = [x for x in groups[1].strip().split(" ") if x != ""]
    
    total = 0
    for n in owned:
        if n in winners:
            total+=1 
    
    result = {
        "id": id_,
        "wins": total,
    }
   
    return result

def solve(filename):
    file = open(filename, "r", encoding="utf-8")

    stack = deque([])
    cards = {}

    for line in file:
        value = parseLine(line)
        cards[value["id"]] = value
        stack.append(value)
    
    file.close()
    
    total = 0
    while stack:
        card = stack.popleft()
        total += 1
        
        for i in range(card["wins"]):
            stack.append(cards[card["id"]+i+1])
    
    return total
    
    
print(solve("input.txt"))