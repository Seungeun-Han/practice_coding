def solution(num_list):
    # a = sum(num_list[1::2])
    # b = sum(num_list[::2])
    # return a if a > b else b
    return max(sum(num_list[::2]), sum(num_list[1::2]))