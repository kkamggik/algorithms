import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    t = int(input())
    if t == 0:
        if not heap: print(0)
        else:
            num = -heapq.heappop(heap)
            print(num)
    else:
        heapq.heappush(heap,-t)