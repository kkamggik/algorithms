import heapq
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = []
    for num in arr: heapq.heappush(heap, num)
    answer = 0
    while len(heap) >= 2:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        summ = x+y
        answer += summ
        heapq.heappush(heap, summ)
    print(answer)