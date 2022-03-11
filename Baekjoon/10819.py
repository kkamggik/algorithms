import sys
input = sys.stdin.readline
def backtracking(idx, curr, summ, cnt):
    if cnt == n:
        global answer
        answer = max(answer, summ)
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(i, arr[i], summ+abs(curr-arr[i]), cnt+1)
            visited[i] = 0
n = int(input())
arr = list(map(int, input().split()))
visited = [0]*n
answer = 0
for i in range(n):
    visited[i] = 1
    backtracking(i, arr[i], 0, 1)
    visited[i] = 0
print(answer)