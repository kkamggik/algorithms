from collections import deque
tests = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dirc = [1, 0, 3, 2]
for t in range(tests):
    n, m, k = map(int, input().split())
    virus = []
    for i in range(k):
        y, x, cnt, d = map(int, input().split())
        virus.append([x, y, cnt, d-1])
    for _ in range(m):
        arr = [[[] for i in range(n)] for j in range(n)]
        for x, y, cnt, d in virus:
            nx, ny = x + dx[d], y + dy[d]
            arr[ny][nx].append([cnt, d])
        virus = []
        for i in range(n):
            for j in range(n):
                if(len(arr[i][j]) >= 1):
                    arr[i][j].sort(key=lambda x: -x[0])
                    d = arr[i][j][0][1]
                    total = 0
                    for k in range(len(arr[i][j])):
                        total += arr[i][j][k][0]
                    if(i == 0 or j == 0 or j == n-1 or i == n-1):
                        total = total // 2
                        d = dirc[d]
                    virus.append([j, i, total, d])
    answer = 0
    for x, y, cnt, d in virus: answer += cnt
    print("#{} {}".format(t+1, answer))
