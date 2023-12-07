NUMBERS = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def isDigit(char: chr) -> bool:
    return ('0' <= char <= '9')

def isStringDigit(string:str)->int:
    for n in NUMBERS:
        if string.find(n) == 0:
            return NUMBERS[n]

    return -1

def isStringDigitEnd(string:str)->int:
    for n in NUMBERS:
        if string.find(n) != -1 and string.find(n) == len(string) - len(n):
            return NUMBERS[n]

    return -1

def solve(filename: str) -> int:
    file = open(filename, "r", encoding="utf-8")
    total = 0
    
    for line in file:
        stripped = line.strip()
        l, r = 0, len(stripped)-1
        ln = -1
        rn = -1
        
        while l <= r:
            left_match  = stripped[l:l+min(r-l, 5)]
            right_match = stripped[r-min(r-l, 4):r+1]

            # left check
            if isDigit(stripped[l]):
                ln = int(stripped[l])
            elif isStringDigit(left_match)!=-1:
                ln = isStringDigit(left_match)
            else:
                l+=1

            # right check
            if isDigit(stripped[r]):
                rn = int(stripped[r])
            elif isStringDigitEnd(right_match)!=-1:
                rn = isStringDigitEnd(right_match)
            else:
                r -= 1
                                      
            # termination case
            if rn != -1 and ln != -1:
                break
        
        # print(f"{stripped} => {ln*10 + rn}")
        total +=  ln * 10 + rn   

    return total
        
    

print(solve(r"C:\Users\marco\Workspace\challenges\adventofcode2023\01\input1.txt"))