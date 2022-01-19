def dfs(idx):
    global rst
    visited[idx] = True
    cycle.append(idx)
    nxt = arr[idx]
    if visited[nxt]:
        if nxt in cycle:
            rst += cycle[cycle.index(nxt):]
        return
    else:
        dfs(nxt)
tests = int(input())
for t in range(tests):
    n = int(input())
    arr = [0]+list(map(int, input().split()))
    visited = [False]*(n+1)
    rst = []
    for i in range(1,n+1):
        if visited[i] == False:
            cycle = []
            dfs(i)
    print(n-len(rst))