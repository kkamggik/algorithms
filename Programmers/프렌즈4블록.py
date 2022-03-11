from collections import deque
def solution(m, n, arr):
    answer = 0
    board = []
    for line in arr:
        board.append(list(line))
    check = False
    while not check:
        check = True
        visited = [[0]*n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!=-1 and (board[i][j] == board[i+1][j] == board[i+1][j+1] == board[i][j+1]):
                    check = False
                    visited[i][j] = 1
                    visited[i][j+1] = 1
                    visited[i+1][j] = 1
                    visited[i+1][j+1] = 1
        queue = deque()
        for i in range(n):
            for j in range(m):
                if visited[j][i] == 0 and board[j][i]!=-1:
                    queue.append(board[j][i])
            idx = m-1
            while queue:
                x = queue.pop()
                board[idx][i] = x
                idx -= 1
            for j in range(idx, -1, -1):
                board[j][i] = -1
    for i in range(m):
        for j in range(n):
            if board[i][j]==-1: answer += 1
    return answer
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))