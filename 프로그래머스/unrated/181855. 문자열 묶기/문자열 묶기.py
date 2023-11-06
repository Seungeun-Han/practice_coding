def solution(strArr):
    count_dict = {}
    
    for l in strArr:
        if len(l) not in count_dict.keys():
            count_dict[len(l)] = 0
        count_dict[len(l)] += 1
    
    return max(count_dict.values())