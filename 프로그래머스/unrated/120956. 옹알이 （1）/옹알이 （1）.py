import itertools

def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    
    possible = can.copy()
    for i in range(2, 5):
        possible += list(map(list, itertools.permutations(can, i)))
    possible = [''.join(i) for i in possible]

    answer = len([0 for i in babbling if i in possible])
    
    return answer


# def solution(babbling):
#     c = 0
#     for b in babbling:
#         for w in [ "aya", "ye", "woo", "ma" ]:
#             if w * 2 not in b:
#                 b = b.replace(w, ' ')
#         if len(b.strip()) == 0:
#             c += 1
#     return c