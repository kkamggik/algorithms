def find(x,parents):
    if parents[x]==x: return parents[x]
    parents[x] = find(parents[x],parents)
    return parents[x]
def union(a,b,parents):
    x = find(a,parents)
    y = find(b,parents)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x
def solution(n, wires):
    answer = 1e9
    arr = [[0]*(n+1) for _ in range(n+1)]
    for a,b in wires:
        arr[a][b] = 1
        arr[b][a] = 1
    for a,b in wires:
        arr[a][b] = 0
        arr[b][a] = 0
        parents = [i for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if arr[i][j]==1:
                    union(i,j,parents)
        arr[a][b] = 1
        arr[b][a] = 1
        for i in range(1,n+1):
            parents[i] = find(i,parents)
        one = parents[1:].count(1)
        other = n - one
        answer = min(answer,abs(one-other))
        print(parents)
    return answer
print(solution(	7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))