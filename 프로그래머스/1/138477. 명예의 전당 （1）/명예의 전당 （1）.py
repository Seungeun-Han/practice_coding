import heapq

def solution(k, score):
    answer = []
    top_k = []

    for s in score:
        if len(top_k) < k:
            heapq.heappush(top_k, s)
        else:
            if top_k[0] < s:
                heapq.heappop(top_k)
                heapq.heappush(top_k, s)
        answer.append(top_k[0])
        
    return answer