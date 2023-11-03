def solution(str_list):
    for i, v in enumerate(str_list):
        if v in ['l', 'r']:
            idx, value = i, v
            break
            
    return str_list[:i] if v=='l' else str_list[i+1:]