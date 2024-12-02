def loadMatrix(filename):
    file = open(filename, "r", encoding="utf-8")
    matrix = []
    counter = 0

    for line in file:
        row = []
        number = 0
        start = -1

        for j,char in enumerate(line.strip()):
            # se trovo un digit, me lo segno
            if char.isdigit():
                if start == -1:
                    counter += 1
                    start = j

                number = number * 10 + int(char)
                
            # se trovo un carattere
            else:
                # verifico se avevo già trovato digit
                if start != -1:
                    for x in range(start, j):
                        row.append((f'N{counter}', int(number)))
                    number = 0
                    start = -1
                
                if char != '*':
                    row.append(('.', 0))
                else:
                    row.append(('*', 0))

        # se non ho messo l'ultimo carattere
        if start != -1:
            for x in range(start, len(line.strip())):
                row.append((f'N{counter}', int(number)))
            
        matrix.append(row)
    
    file.close()
    return matrix

def debugPrint(matrix, y_before, y_after, row, x_start, x_end):
    if y_before != -1:
        print(f"{matrix[y_before][x_start:x_end+1]}")
    print(f"{matrix[row][x_start:x_end+1]}\t\t\t in row {row}")
    if y_after != -1:
        print(f"{matrix[y_after][x_start:x_end+1]}")
    print("")


def check(matrix, x, y):
    x_start = x - 1 if x > 0 else 0
    x_end   = x + 1 if x < len(matrix[0])-1 else x
    
    rows = [y]
    if y > 0:               rows.append(y-1)
    if y < len(matrix)-1:   rows.append(y+1)

    values = {}
    for z in range(x_start, x_end+1):
        for row in rows:
            if 'N' in matrix[row][z][0]:
                values[matrix[row][z][0]] = matrix[row][z][1]

    if len(values) == 2:
        # debugPrint(matrix, y_before, y_after, y, x_start, x_end)
        prod = 1
        for key in values:
            prod *= values[key] 

        return prod
    
    return 0
    

def solve(filename):
    matrix = loadMatrix(filename)   
    total = 0
        
    for i, row in enumerate(matrix):
        for j, ceil in enumerate(row):
            if ceil[0] == '*':
                total += check(matrix,j,i) 
   
    return total


print(solve(r"C:\Users\marco\Workspace\challenges\adventofcode2023\03\input.txt"))