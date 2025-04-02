def solution(s):
    answer = [-1]*len(s)
    dic = {}
    
    for i, v in enumerate(s):
        if v in dic:
            answer[i] = i-dic[v]
            dic[v] = i
        else:
            dic[v] = i
    
    return answer