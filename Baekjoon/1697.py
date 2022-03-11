from collections import deque
n,k = map(int, input().split())
queue = deque()
visit = [-1]*100001
visit[n] = 0
queue.append(n)
while queue:
    x = queue.popleft()
    if k==x: break
    if x-1 >= 0 and visit[x-1] == -1:
        visit[x-1] = visit[x]+1
        queue.append(x-1)
    if x+1 <= 100000 and visit[x+1] == -1:
        visit[x+1] = visit[x]+1
        queue.append(x+1)
    if x*2 <= 100000 and visit[x*2] == -1:
        visit[x*2] = visit[x]+1
        queue.append(x*2)
print(visit[k])