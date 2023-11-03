# def solution(str_list):
#     for i, v in enumerate(str_list):
#         if v in ['l', 'r']:
#             idx, value = i, v
#             break
            
#     return str_list[:i] if v=='l' else str_list[i+1:]


def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': return str_list[:i]
        elif str_list[i]=='r': return str_list[i+1:]
    return []