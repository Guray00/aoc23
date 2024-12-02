import math

def readfile(filename):
    
    file = open(filename, "r", encoding="utf-8")
    
    times       = [int(x) for x in file.readline().replace("Time:", "").strip().split(" ") if x != " " and x!=""]
    distances   = [int(x) for x in file.readline().replace("Distance:", "").strip().split(" ") if x != " " and x!=""]
    
    file.close()

    return times, distances
    
    
def first_part(times, distances):
    total = 1 

    for i, time in enumerate(times):
        count = 0 
        # -x^2 + x*time -distance[i]
        min_val = math.ceil((times[i] - math.sqrt(times[i] ** 2 - 4 * distances[i])) / 2 )
        max_val = math.floor((times[i] + math.sqrt(times[i] ** 2 - 4 * distances[i])) / 2) 
        
        total *= (max_val - min_val + 1)
    return total

def second_part(times, distances):
    times =     [int("".join([str(x) for x in times]))]
    distances = [int("".join([str(x) for x in distances]))]
    
    return first_part(times, distances)
        
    
times, distances = readfile("input.txt")
    
print(first_part(times, distances))
print(second_part(times, distances))



""" 
        for x in range(1, time+1):
            if (time-x)*x > distances[i]: 
                # print(f"time: {time} distance: {distances[i]} con x: {x}")
                count += 1
"""