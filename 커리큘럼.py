from collections import deque
n = int(input())
arr = [[] for _ in range(n+1)]
time = [0]*(n+1)
indegree = [0]*(n+1)
rst = [0]*(n+1)
for i in range(1,n+1):
    lst = list(map(int, input().split()))
    time[i] = lst[0]
    rst[i] = time[i]
    nlst = lst[1:-1]
    for j in nlst:
        indegree[i] += 1
        arr[j].append(i)
queue = deque()
for i in range(1,n+1):
    if indegree[i]==0:
        queue.append(i)
while queue:
    now = queue.popleft()
    for i in arr[now]:
        rst[i] = max(rst[i], rst[now]+time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
for i in range(1,n+1):
    print(rst[i])