# def solution(num_list):
#     answer = 0
    
#     for n in num_list:
#         if n == 1: 
#             continue 
#         for i in range(1, 5):
#             if n >= 2**i and n < 2**(i+1):
#                 answer += i
#                 break
        
#     return answer


def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)