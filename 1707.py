def dfs(idx, flag):
    visited[idx] = flag
    for adj in arr[idx]:
        if visited[adj] == 0:
            if not dfs(adj,-flag): return False
        elif visited[adj] == flag: return False
    return True
tests = int(input())
for t in range(tests):
    v,e = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    visited = [0]*(v+1)
    answer = 'YES'
    for i in range(1,v+1):
        if visited[i] == 0:
            bipartite = dfs(i,1)
            if not bipartite: 
                answer = 'NO'
                break
    print(answer)
