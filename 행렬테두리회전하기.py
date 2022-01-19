def solution(n, m, queries):
    answer = []
    arr = [[0]*m for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(m):
            arr[i][j] = num
            num += 1
    for query in queries:
        y1,x1,y2,x2 = query
        y1,x1,y2,x2 = y1-1,x1-1,y2-1,x2-1
        mn = 1e9
        prev = arr[y1+1][x1]
        for i in range(x1,x2+1):
            mn = min(mn,prev)
            nxt = arr[y1][i] 
            arr[y1][i] = prev 
            prev = nxt
        for i in range(y1+1,y2+1):
            mn = min(mn,prev)
            nxt = arr[i][x2]
            arr[i][x2] = prev
            prev = nxt
        for i in range(x2-1,x1-1,-1):
            mn = min(mn,prev)
            nxt = arr[y2][i]
            arr[y2][i] = prev
            prev = nxt
        for i in range(y2-1,y1-1,-1):
            mn = min(mn,prev)
            nxt = arr[i][x1]
            arr[i][x1] = prev
            prev = nxt
        answer.append(mn)
    return answer

print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))