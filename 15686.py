from itertools import combinations
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2: chicken.append([j,i])
        if arr[i][j] == 1: house.append([j,i])
answer = 2e9
for i in range(1, m+1):
    combination = combinations(chicken, i)
    for com in combination:
        dist = 0
        for h in house:
            tdist = 2e9
            for chick in com:
                tdist = min(tdist, abs(chick[0]-h[0])+abs(chick[1]-h[1]))
            dist += tdist
        answer = min(answer, dist)
print(answer)