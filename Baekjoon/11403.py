import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j]==1 or (arr[i][k]==1 and arr[k][j]==1):
                arr[i][j] = 1
for i in arr:
    for j in i: print(j, end=' ')
    print()