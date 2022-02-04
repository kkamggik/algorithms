import sys
input = sys.stdin.readline
def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    a = find(x)
    b = find(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
gate = int(input())
plane = int(input())
parent = [i for i in range(gate+1)]
planes = [int(input()) for _ in range(plane)]
answer = 0
for p in planes:
    x = find(p)
    if x == 0: break
    union(x, x-1)
    answer += 1
print(answer)
