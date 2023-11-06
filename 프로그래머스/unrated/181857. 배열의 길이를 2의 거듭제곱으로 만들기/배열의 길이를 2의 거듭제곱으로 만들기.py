def solution(arr):
    exp = len(bin(len(arr)))-2
    return arr if len(arr) == 2**(exp-1) else arr + [0]*(2**exp-len(arr))