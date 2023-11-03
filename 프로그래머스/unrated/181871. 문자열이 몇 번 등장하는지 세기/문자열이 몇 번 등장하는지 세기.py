def solution(myString, pat):
#     answer = 0

#     for i in range(len(myString)):
#         if pat == myString[i:i+len(pat)]:
#             answer += 1

#     return answer
    return sum(myString[i:i + len(pat)] == pat for i in range(len(myString)))