def solution(board, skill):
    answer = 0
    summ = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for t,r1,c1,r2,c2,degree in skill:
        if t == 1:
            summ[r1][c1] -= degree
            summ[r1][c2+1] += degree
            summ[r2+1][c1] += degree
            summ[r2+1][c2+1] -= degree
        else:
            summ[r1][c1] += degree
            summ[r1][c2+1] -= degree
            summ[r2+1][c1] -= degree
            summ[r2+1][c2+1] += degree
    # 누적합 계산
    # 1. 위에서 아래로
    for i in range(len(summ[0])):
        prev = summ[0][i]
        for j in range(1,len(summ)):
            prev += summ[j][i]
            summ[j][i] = prev
    # 2. 왼쪽에서 오른쪽으로
    for i in range(len(summ)):
        prev = summ[i][0]
        for j in range(1, len(summ[0])):
            prev += summ[i][j]
            summ[i][j] = prev
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += summ[i][j]
            if board[i][j] > 0: answer+=1
    return answer