def solution(board, k):
    answer = 0
    for i in range(k+1):
        if i >= len(board):
            break
        answer += sum(board[i][:k-i+1])
    return answer