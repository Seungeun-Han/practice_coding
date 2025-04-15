import copy
def harzardous(i, j, check, n):
    x = [-1, 0, 1, -1, -1, 1, 0, 1]
    y = [-1, -1, -1, 0, 1, 0, 1, 1]
    
    for dx, dy in zip(x, y):
        if i+dx > -1 and j+dy > -1 and i+dx < n and j+dy < n:
            check[i+dx][j+dy] = 1
        
    return check
        

def solution(board):
    answer = 0
    n = len(board)
    check = copy.deepcopy(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                check = harzardous(i, j, check, n)
    
    return sum([len([i for i in c if i == 0]) for c in check])