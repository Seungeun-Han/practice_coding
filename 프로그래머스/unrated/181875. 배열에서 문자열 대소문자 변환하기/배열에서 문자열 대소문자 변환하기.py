def solution(strArr):
    answer = []
        
    return [strArr[i].upper() if i%2 else strArr[i].lower() for i, string in enumerate(strArr)]