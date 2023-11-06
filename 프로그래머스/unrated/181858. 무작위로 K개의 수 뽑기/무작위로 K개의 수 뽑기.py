def solution(arr, k):
    answer = []
    set_answer = list(set(arr))
    
    for i in arr:
        if len(answer)==k:
            return answer
        if i not in answer:
            answer.append(i)
        
    return answer+[-1]*(k - len(answer))