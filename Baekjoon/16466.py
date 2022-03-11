import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
heap = []
for num in arr: heapq.heappush(heap, num)
answer = 1
while heap:
    if heap[0] != answer:
        break
    heapq.heappop(heap)
    answer += 1
print(answer)