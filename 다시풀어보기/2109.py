import sys
import heapq
input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    p,d = map(int, input().split())
    nums.append([p,d])
nums.sort(key = lambda x:x[1])
sums = []
for num in nums:
    heapq.heappush(sums, num[0])
    if len(sums) > num[1]:
        heapq.heappop(sums)
print(sum(sums))