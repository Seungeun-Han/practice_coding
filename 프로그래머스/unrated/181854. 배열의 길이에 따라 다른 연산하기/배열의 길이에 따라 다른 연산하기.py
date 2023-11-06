def solution(arr, n):
    return [v+n*int(i%2) if int(len(arr)%2==0) else v+n*int((i+1)%2) for i, v in enumerate(arr)]