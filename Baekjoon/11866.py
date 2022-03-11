from collections import deque
n,m = map(int, input().split())
queue = deque()
for i in range(1,n+1): queue.append(i)
print("<",end="")
while queue:
    for i in range(m-1):
        queue.append(queue[0])
        x = queue.popleft()
    print(queue.popleft(),end="")
    if queue: print(", ",end="")
print(">")