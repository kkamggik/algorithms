import heapq
import sys
input = sys.stdin.readline
n = int(input())
cups = []
for _ in range(n):
    d,c = map(int, input().split())
    cups.append([d,c])
cups.sort(key = lambda x:x[0])
heap = []
for cup in cups:
    heapq.heappush(heap, cup[1])
    if len(heap) > cup[0]:
        heapq.heappop(heap)
print(sum(heap))
