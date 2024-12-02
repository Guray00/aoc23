from collections import deque
from operator import itemgetter

# leggo il file di input
def readfile(filename):
    file = open(filename, "r", encoding="utf-8")
    
    result = deque([])
    for line in file:
        result.append(line.strip().split(" "))
    
    file.close()
    return result


def get_strength(card, jolly=False):
    values = {}
    
    jolly_counter = 0
    for char in card[0]:
        if jolly and char == 'J': 
            jolly_counter += 1
            continue

        values[char]  = values.get(char,0) + 1
    
    order = [x[1] for x in sorted(values.items(), key=itemgetter(1), reverse=True)]
    
    # se ho un jolly lo metto in posizione più vantaggiosa
    if   jolly and order == []: order.append(5)
    elif jolly: order[0] += jolly_counter
    
    if   order[0] == 5: return 6                                # five of a kind
    elif order[0] == 4: return 5                                # four of a kind
    elif order[0] == 3 and order[1] == 2: return 4              # full house
    elif order[0] == 3 and order[1] == order[2] == 1: return 3  # three of a kind
    elif order[0] == order[1] == 2: return 2                    # two pairs
    elif order[0] == 2: return 1                                # one pair
    else: return 0                                              # height card
      

# converto la mano in un numero
def hand_to_num(hand, jolly=False):
    if not jolly:
        ordering_map = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
    else:
        ordering_map = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}

    value = 0
    for char in hand:
        value = value*13 + ordering_map[char] # converto in base 13
            
    return value

def calculate_total(hands, jolly):
    strength = [[],[],[],[],[],[],[]]
    
    for hand in hands:
        index = get_strength(hand, jolly)
        strength[index].append((hand_to_num(hand[0], jolly), int(hand[1])))
    
    rank = 1
    total = 0
    for s in strength:
        ordinato = sorted(s, key=lambda x: x[0])
        
        for x in ordinato:
            total += rank *  x[1]
            rank += 1

    return total
               
def first_part(hands):
    return calculate_total(hands, False)

def second_part(hands):
    return calculate_total(hands, True)

hands = readfile("input.txt")
print(first_part(hands))
print(second_part(hands))