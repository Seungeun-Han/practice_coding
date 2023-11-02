def solution(my_string):
    answer = [0 for i in range(52)]

    for v in my_string:
        if v.isupper():
            answer[ord(v)-65] += 1
        else:
            answer[ord(v)-97+26] += 1

    return answer