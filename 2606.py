from collections import deque
def visit(start):
    v = [0]*(n+1)
    v[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for dx in range(1,n+1):
            if arr[x][dx] and v[dx]==0:
                v[dx] = 1
                queue.append(dx)
    return v
n = int(input())
m = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
v = visit(1)
print(v.count(1) - 1)