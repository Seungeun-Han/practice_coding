def solution(num_list):
    answer = [i for i, v in enumerate(num_list) if v<0]

    return answer[0] if len(answer)>0 else -1