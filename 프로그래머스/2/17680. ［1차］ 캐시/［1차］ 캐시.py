from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = ['']*cacheSize
    d = deque(cache, maxlen=cacheSize)
    
    for ct in cities:
        ct = ct.lower()

        if ct in d:  # cache hit
            d.remove(ct)
            d.append(ct)
            answer += 1
        elif ct not in d:  # cache miss
            d.append(ct)
            answer += 5

    return answer