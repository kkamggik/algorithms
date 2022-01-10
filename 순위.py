def solution(n, results):
    answer = 0
    arr = [[0]*(n+1) for _ in range(n+1)]
    for a,b in results:
        arr[a][b] = 1
        arr[b][a] = -1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if arr[i][j] == 0:
                    if arr[i][k] == 1 and arr[k][j] == 1: arr[i][j] = 1
                    elif arr[i][k] == -1 and arr[k][j] == -1: arr[i][j] = -1
    answer = 0
    for i in range(1,n+1):
        win = arr[i][1:].count(-1)
        lose = arr[i][1:].count(1)
        if win+lose == n-1: answer+=1
    return answer
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))