import heapq
import sys
input = sys.stdin.readline
n = int(input())
locations = []
answer = 0
for _ in range(n):
    h,o = map(int, input().split())
    if h > o: h,o = o,h
    locations.append([h,o])
m = int(input())
locations.sort(key = lambda x:(x[1],x[0]))
line = []
for location in locations:
    house, office = location
    heapq.heappush(line, [house, office])
    while line and office-line[0][0] > m:
        heapq.heappop(line)
    answer = max(answer, len(line))
print(answer)