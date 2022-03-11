import sys
input = sys.stdin.readline
n,m = map(int, input().split())
names = {}
for i in range(1,n+1):
    name = input().strip()
    names[name] = i
    names[str(i)] = name
for _ in range(m):
    x = input().strip()
    print(names[x])
