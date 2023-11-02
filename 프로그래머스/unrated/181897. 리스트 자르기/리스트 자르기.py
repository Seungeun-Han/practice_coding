def solution(n, slicer, num_list):
    a = 0 if n==1 else slicer[0]
    b = len(num_list) if n==2 else slicer[1]+1
    c = slicer[2] if n==4 else 1
    return num_list[a:b:c]