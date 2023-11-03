def solution(arr, query):
    answer = arr
    for i, q in enumerate(query):
        answer = answer[:(q+1)] if i%2==0 else answer[q:]
    return answer