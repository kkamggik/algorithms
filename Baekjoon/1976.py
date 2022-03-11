import sys
input = sys.stdin.readline
def find(x):
    if parents[x] == x: return x
    parents[x] = find(parents[x])
    return parents[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
n = int(input())
parents = [i for i in range(n)]
m = int(input())
arr = []
for _ in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
for i in range(n):
    for j in range(i+1,n):
        if arr[i][j] == 1:
            union(i,j)
routes = list(map(int, input().split()))
route = find(routes[0]-1)
ans = 'YES'
for r in routes[1:]:
    if route != find(r-1):
        ans = 'NO'
        break
print(ans)