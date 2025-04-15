def solution(survey, choices):
    answer = ''
    score = {'R': 0, 'T':0, 'C': 0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i, s in enumerate(survey):
        n, m = s[0], s[1]
        if choices[i] > 4:
            score[m] += choices[i]%4
        elif choices[i] < 4:
            score[n] += 4-choices[i]
    
    person_type = ['RT', 'CF', 'JM', 'AN']
    for t in person_type:
        if score[t[0]] > score[t[1]]:
            answer += t[0]
        elif score[t[0]] == score[t[1]]:
            answer += t[0]
        else:
            answer += t[1]

    return answer