import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
lst = [list(map(int,input().strip())) for _ in range(n)]
def flip(x,y):
    global arr
    for i in range(y,y+3):
        for j in range(x,x+3):
            arr[i][j] = 1-arr[i][j]
answer = 0
for i in range(n-2):
    for j in range(m-2):
        if arr[i][j] != lst[i][j]:
            flip(j,i)
            answer += 1
for i in range(n):
    for j in range(m):
        if arr[i][j] != lst[i][j]:
            answer = -1
            break
print(answer)