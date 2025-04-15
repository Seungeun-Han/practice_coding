def solution(k, m, score):
    answer = 0
    sorted_score = sorted(score)[::-1]
    
    for i in range(len(score)//m):
        if i*m+m-1 > len(sorted_score):
            break
        answer += sorted_score[i*m+m-1]*m

    return answer