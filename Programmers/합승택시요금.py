def solution(n, s, a, b, fares):
    answer = 1e9
    costs = [[1e9]*(n+1) for _ in range(n+1)]
    for fare in fares:
        x,y,c = fare
        costs[x][y] = c
        costs[y][x] = c
    for i in range(n+1):
        costs[i][i] = 0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                costs[i][j] = min(costs[i][j], costs[i][k]+costs[k][j])
    for i in range(1,n+1):
        together = costs[s][i]
        apeach,muzi = costs[i][a],costs[i][b]
        answer = min(answer, together+apeach+muzi)
    return answer
print(solution(	7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))