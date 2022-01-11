def find(x):
    if parents[x] == x: return x
    parents[x] = find(parents[x])
    return parents[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parents[b] = a
        friends[a] += friends[b]
t = int(input())
for _ in range(t):
    n = int(input())
    friends = {}
    parents = {}
    for i in range(n):
        n1,n2 = map(str, input().split())
        if n1 not in parents:
            parents[n1] = n1
            friends[n1] = 1
        if n2 not in parents:
            parents[n2] = n2
            friends[n2] = 1
        union(n1,n2)
        print(friends[find(n1)])
