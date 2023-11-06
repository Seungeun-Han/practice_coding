def solution(rank, attendance):
    answer = sorted([[rank[i], i] for i, v in enumerate(attendance) if v])

    return 10000*answer[0][1] + 100*answer[1][1] + answer[2][1]