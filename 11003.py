from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque()
for i in range(n):
    num = arr[i]
    while queue and queue[-1][1] > num: queue.pop()
    while queue and queue[0][0] < i - m + 1: queue.popleft()
    queue.append([i, num])
    print(queue[0][1], end=' ')
    
