import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
n = int(input())
for _ in range(n):
    cm = list(map(str, input().split()))
    if cm[0] == 'push':
        queue.append(cm[1])
    elif cm[0] == 'pop':
        if queue:
            x = queue.popleft()
            print(x)
        else: print(-1)
    elif cm[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif cm[0] == 'back':
        if queue: print(queue[-1])
        else: print(-1)
    elif cm[0] == 'size':
        print(len(queue))
    elif cm[0] == 'empty':
        if queue: print(0)
        else: print(1)