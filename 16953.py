from collections import deque
n,m = map(int, input().split())
queue = deque()
queue.append([n,1])
flag = False
while queue:
    val, cnt = queue.popleft()
    if val == m:
        flag = True
        break
    if val > m: continue
    queue.append([val*2, cnt+1])
    queue.append([val*10 + 1, cnt+1])
if flag == True: print(cnt)
else: print(-1)