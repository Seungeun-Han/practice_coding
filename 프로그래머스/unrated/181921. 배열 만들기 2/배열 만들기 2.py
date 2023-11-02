def solution(l, r):
    answer = [i for i in range(l, r + 1) if not(set(str(i))-{'0', '5'})]
    return answer if len(answer)>0 else [-1]
