def solution(arr):
    max_num = max(len(arr), len(arr[0]))
    answer = [[i for i in range(max_num)] for j in range(max_num)]
    
    for i in range(max_num):
        for j in range(max_num):
            if i >= len(arr):
                answer[i][j] = 0
                continue
            elif j >= len(arr[0]):
                answer[i][j] = 0
                continue
            answer[i][j] = arr[i][j]
    
    return answer