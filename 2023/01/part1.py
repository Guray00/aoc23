
def isDigit(char: chr) -> bool:
    return ('0' <= char <= '9')

def solve(filename: str) -> int:
    file = open(filename, "r", encoding="utf-8")
    total = 0
    
    for line in file:
        stripped = line.strip()
        l, r = 0, len(stripped)-1
        
        while l <= r:
            if not isDigit(stripped[l]):
                l += 1
            elif not isDigit(stripped[r]):
                r -= 1
            else:
                break
        
        total += int(stripped[l]) * 10 + int(stripped[r])
    
    return total
        
    

print(solve("./input1.txt"))