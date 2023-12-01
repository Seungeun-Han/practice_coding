import itertools

def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    
    possible = can.copy()
    for i in range(2, 5):
        possible += list(map(list, itertools.permutations(can, i)))
    possible = [''.join(i) for i in possible]

    answer = len([0 for i in babbling if i in possible])
    
    return answer