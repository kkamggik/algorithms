from collections import deque
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = deque()
    for i in range(n):
        queue.append([arr[i],i])
    order = 0
    while queue:
        item,idx = queue.popleft() 
        flag = 0
        for i in range(len(queue)):
            if queue[i][0] > item:
                flag = 1
                break
        if flag == 1:
            queue.append([item,idx])
        else:
            order += 1
            if idx == m: break
    print(order)
