def solution(phone_book):
    answer = True
    sorted_pb = sorted(phone_book)
    for i in range(len(sorted_pb) - 1) :
        if sorted_pb[i+1].startswith(sorted_pb[i]) : return False
    return answer