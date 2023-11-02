def solution(arr):
    answer = [i for i, v in enumerate(arr) if v==2]
    return arr[answer[0]:answer[-1]+1] if len(answer)>0 else [-1]