import heapq
import sys
input = sys.stdin.readline
n = int(input())
tables = []
for _ in range(n):
    s,e = map(int, input().split())
    tables.append([s,e])
tables.sort()
rooms = []
for s,e in tables:
    if not rooms: heapq.heappush(rooms, e)
    else:
        if rooms[0] <= s:
            heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        else:
            heapq.heappush(rooms, e)
print(len(rooms))