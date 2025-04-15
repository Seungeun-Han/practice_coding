# 재귀로 풀면 시간 초과
# def dfs(i, j, triangle):
#     if i == len(triangle) - 1:
#         return triangle[i][j]
#     return triangle[i][j] + max(dfs(i + 1, j, triangle), dfs(i + 1, j + 1, triangle))

# def solution(triangle):  
#     return dfs(0, 0, triangle)

# DP로 풀어야 함
def solution(triangle): 
    answer = 0
    
    dp_triangle = triangle[::-1]
    for i in range(1, len(dp_triangle)):
        for j in range(len(dp_triangle[i])):
            dp_triangle[i][j] += max(dp_triangle[i-1][j], dp_triangle[i-1][j+1])

    return dp_triangle[-1][0]
    