from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()
for i in range(n):
    t = int(input())
    if t!=0: queue.append(t)
    else: queue.pop()
print(sum(queue))