import sys
input = sys.stdin.readline
n = int(input())
coords = []
for _ in range(n):
    x,y = map(int, input().split())
    coords.append([x,y])
# coords.sort(key = lambda x:(x[0],x[1]))
coords.sort()
for x,y in coords:
    print(x,y)