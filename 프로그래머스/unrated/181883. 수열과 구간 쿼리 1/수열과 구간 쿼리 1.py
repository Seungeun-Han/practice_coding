def solution(arr, queries):
    answer = arr
    for s, e in queries:
        answer = answer[:s] + [i+1 for i in answer[s:e+1]] + answer[e+1:]
    return answer