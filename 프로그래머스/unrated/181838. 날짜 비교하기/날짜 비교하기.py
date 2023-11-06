def combine(date):
    return ''.join([i.zfill(2) for i in list(map(str, date))])

def solution(date1, date2):
    # return int(combine(date1) < combine(date2))
    return int(date1 < date2)