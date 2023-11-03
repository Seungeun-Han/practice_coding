def solution(arr):
    present = arr
    previous = []
    count=0
    
    while 1:
        if previous == present:
            return count - 1
        previous = present
        present = [i // 2 if (i >= 50 and i % 2 == 0) else (i * 2+1 if (i < 50 and i % 2 != 0) else i) for i in previous]
        count += 1