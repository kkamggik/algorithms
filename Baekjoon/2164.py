from collections import deque
queue = deque()
n = int(input())
for i in range(n,0,-1):
    queue.append(i)
while len(queue)!=1:
    queue.pop()
    x = queue.pop()
    queue.appendleft(x)
print(queue[0])
