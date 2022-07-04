T = int(input())
def smash(x,y,k,arr):
    t  = 0
    for yy in range(y,y+k):
        for xx in range(x,x+k):
            t += arr[yy][xx]
    return t
for test_case in range(1, T + 1):
    n,k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rst = 0
    for i in range(n-k+1):
        for j in range(n-k+1):
            rst = max(rst, smash(j,i,k,arr))
    print(rst)