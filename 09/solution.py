import copy

def readfile(filename):
    file = open(filename, "r", encoding="utf-8")
    
    histories = []
    for line in file:
        histories.append([int(x) for x in line.strip().split(" ")])
    
    file.close()
    return histories

def first_part(histories):
    total = 0
    for history in histories:
        current = history
        
        # ending = []
        all_zeroes = False 

        while(not all_zeroes):
            all_zeroes = True
            
            # ending.append(current[-1])
            total += current[-1]
            for i in range(len(current)-1):
                current[i] = current[i+1] - current[i]

                if current[i] != 0:
                    all_zeroes = False
            
            current.pop()
            # print(current)
        
    return total        

def second_part(histories):

    total = 0
    for history in histories:
        current = history
        # print(f"comincio {current}")
        
        beginning = []
        all_zeroes = False 

        while(not all_zeroes):
            all_zeroes = True
            
            beginning.append(current[0])
            for i in range(len(current)-1):
                current[i] = current[i+1] - current[i]

                if current[i] != 0:
                    all_zeroes = False
            
            current.pop()
            # print(f"{current}")
        
        partial = 0
        for x in beginning[::-1]:
            partial = x - partial
        
        total += partial
        
    return total        




histories = readfile("input.txt")
h1 = copy.deepcopy(histories)
h2 = copy.deepcopy(histories)
print(first_part(h1))
print(second_part(h2))