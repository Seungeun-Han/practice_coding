def solution(n):
    return sum([i if n%2 else i**2 for i in range(n, 0, -2)])