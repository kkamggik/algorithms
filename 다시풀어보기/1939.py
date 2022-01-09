from collections import deque
def bfs(mid):
    visited[x] = 1
    queue = deque()
    queue.append(x)
    while queue:
        i = queue.popleft()
        if i == y: return True
        for idx,w in arr[i]:
            if visited[idx]==0 and mid<=w:
                visited[idx] = 1
                queue.append(idx)
    return False
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])
x,y = map(int, input().split())
left, right = 1,1000000000
answer = 0
while left <= right:
    mid = (left+right)//2
    visited = [0]*(n+1)
    if bfs(mid):
        left = mid+1
    else:
        right = mid-1
print(right)

