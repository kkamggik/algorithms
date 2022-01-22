def solution(board):
    answer = 0
    n,m = len(board),len(board[0])
    for i in range(n):
        for j in range(m):
            if i==0 or j==0: 
                answer = max(answer, board[i][j])
                continue
            elif board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
            answer = max(answer, board[i][j])
    return answer**2
print(solution([[0, 1]]))