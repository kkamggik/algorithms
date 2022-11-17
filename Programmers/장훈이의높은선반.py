ans = 2e9
visited = []
test = int(input())
arr = []
n, k = 0, 0
def dfs(idx, summ):
    if(summ >= k):
        global ans
        ans = min(ans, summ - k)
        return
    for i in range(idx, n):
        if(visited[i] == 0):
            visited[i] = 1
            dfs(i+1, summ + arr[i])
            visited[i] = 0
for t in range(test):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0]*n
    ans = 2e9
    dfs(0, 0)
    print("#{} {}".format(t+1, ans))
