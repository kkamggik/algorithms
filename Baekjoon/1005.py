from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
tests = int(input())
for t in range(tests):
    n,k = map(int, input().split())
    time = [0]+list(map(int, input().split()))
    arr = [[] for _ in range(n+1)]
    done = [0]*(n+1)
    for _ in range(k):
        a,b = map(int, input().split())
        arr[a].append(b)
        done[b]+=1
    target = int(input())
    dp = [0]*(n+1)
    queue = deque()
    for i in range(1,n+1):
        if done[i] == 0:
            dp[i] = time[i]
            queue.append(i)
    while queue:
        x = queue.popleft()
        for nxt in arr[x]:
            done[nxt]-=1
            dp[nxt] = max(dp[nxt], dp[x]+time[nxt])
            if done[nxt]==0:
                queue.append(nxt)
    print(dp[target])
