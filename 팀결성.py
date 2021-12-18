def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n,m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    c,a,b = map(int, input().split())
    # 팀 합치기
    if c==0:
        union(a,b)
    # 같은 팀 여부 확인
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
