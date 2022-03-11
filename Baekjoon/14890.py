import sys
input = sys.stdin.readline
def check(i, arr):
    check = [0]*n
    # 오르막
    for j in range(1,n):
        if arr[i][j]==arr[i][j-1]: continue
        if arr[i][j]-arr[i][j-1]==1:
            for k in range(j-m, j):
                if k < 0 or check[k]==1 or arr[i][j]-arr[i][k]!=1: return False
                check[k] = 1
        elif abs(arr[i][j]-arr[i][j-1])>1: return False
    for j in range(n-1):
        if arr[i][j]==arr[i][j+1]: continue
        if arr[i][j]-arr[i][j+1]==1:
            for k in range(j+1, j+m+1):
                if k >= n or check[k]==1 or arr[i][j]-arr[i][k]!=1: return False
                check[k] = 1
        elif abs(arr[i][j]-arr[i][j+1])>1: return False
    return True
n,m = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(n)]
lst2 = list(zip(*lst1))
answer = 0
for i in range(n):
    if check(i,lst1)==True: answer+=1
    if check(i,lst2)==True: answer+=1
print(answer)
