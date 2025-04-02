def solution(n):
    answer = [i for i in range(1, 200) if i%3 != 0 and '3' not in str(i)]
    return answer[n-1]