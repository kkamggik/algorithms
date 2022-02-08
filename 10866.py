from collections import deque
n = int(input())
queue = deque()
for _ in range(n):
    cm = input().strip().split()
    if cm[0]=='push_front': queue.appendleft(cm[1])
    elif cm[0]=='push_back': queue.append(cm[1])
    elif cm[0]=='pop_front': 
        if queue: print(queue.popleft())
        else: print(-1)
    elif cm[0]=='pop_back': 
        if queue: print(queue.pop())
        else: print(-1)
    elif cm[0]=='size':
        print(len(queue))
    elif cm[0]=='empty':
        if queue: print(0)
        else: print(1)
    elif cm[0]=='front':
        if queue: print(queue[0])
        else: print(-1)
    elif cm[0]=='back':
        if queue: print(queue[-1])
        else: print(-1)
