def solution(picture, k):
    answer = []

    for i, p in enumerate(picture):
        for j in range(k):
            answer.append(''.join([i*k for i in p]))
    
    return answer