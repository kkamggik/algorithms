def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n+1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            if find(i+1)!=find(j+1): union(i+1,j+1)
visits = list(map(int, input().split()))
first = parent[visits[0]]
ans = 'YES'
for i in visits[1:]:
    if parent[i] != first: 
        ans = 'NO'
        break
print(ans)