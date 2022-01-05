from collections import deque
def bfs(mid):
    queue = deque()
    queue.append(x)
    v[x] = 1
    while queue:
        t = queue.popleft()
        if t == y: return True
        else:
            for tx,tc in arr[t]:
                if v[tx]==0 and mid<=tc:
                    queue.append(tx)
                    v[tx] = 1
    return False
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
ans = 0
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])
x,y = map(int, input().split())
left, right = 1, 1000000000
while left <= right:
    v = [0]*(n+1)
    mid = (left+right)//2
    if bfs(mid): 
        ans = mid
        left = mid+1
    else: right = mid-1
print(ans)