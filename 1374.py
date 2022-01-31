import heapq
import sys
input = sys.stdin.readline
n = int(input())
classes = []
for _ in range(n):
    a,b,c = map(int, input().split())
    classes.append([b,c])
classes.sort()
rooms = []
answer = 0
for c in classes:
    start,end = c
    if not rooms: heapq.heappush(rooms, end)
    else:
        if rooms[0] <= start:
            heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        else:
            heapq.heappush(rooms, end)
    answer = max(answer, len(rooms))
print(answer)