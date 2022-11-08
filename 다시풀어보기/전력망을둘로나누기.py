arr = []
visited = []
def dfs(idx, flag):
    for i in range(1, len(arr)):
        if(arr[idx][i] == 1 and visited[i] == 0):
            visited[i] = flag
            dfs(i, flag)
def solution(n, wires):
    global visited, arr
    answer = 2e9
    arr = [[0]*(n+1) for _ in range(n+1)]
    for a,b in wires:
        arr[a][b] = 1
        arr[b][a] = 1
    
    for a,b in wires:
        arr[a][b] = 0
        arr[b][a] = 0
        cnt = 1
        visited = [0]*(n+1)
        for i in range(1, n+1):
            if(visited[i] == 0):
                visited[i] = cnt
                dfs(i, cnt)
                cnt += 1
        answer = min(answer, abs(visited.count(1) - visited.count(2)))
        arr[a][b] = 1
        arr[b][a] = 1
        
    return answer
