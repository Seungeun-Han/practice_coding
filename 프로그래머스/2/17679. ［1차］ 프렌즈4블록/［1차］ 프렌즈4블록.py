def solution(m, n, board):
    mod_board = [list(i) for i in board]
    delta = [[0, 0], [0, 1], [1, 0], [1, 1]]

    for k in range(1000):
        removed = []
        for i in range(m-1):
            for j in range(n-1):
                roi = [mod_board[i][j], mod_board[i+1][j], mod_board[i][j+1], mod_board[i+1][j+1]]
                # print(set(roi), len(set(roi)))
                if len(set(roi)) == 1:
                    removed.append([i, j])
        # print(k, "remove index list:", removed)

        for i, j in removed:
            for di, dj in delta:
                x, y = i + di, j + dj
                mod_board[x][y] = '0'        
        
        trans_board = [list(''.join([mod_board[i][j] for i in range(m) if mod_board[i][j] != '0']).zfill(m)) for j in range(n)]
        # print(trans_board)
        
        for j in range(n):
            for i in range(m):
                mod_board[i][j] = trans_board[j][i]
                    
    # print(mod_board)
    return sum([m.count('0') for m in mod_board])