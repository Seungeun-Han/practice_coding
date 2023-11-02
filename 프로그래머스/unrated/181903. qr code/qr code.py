def solution(q, r, code):
    # answer = ''
    # i=0
    # while i*q+r < len(code):
    #     answer += code[i*q+r]
    #     i += 1
    # return answer
    return code[r::q]