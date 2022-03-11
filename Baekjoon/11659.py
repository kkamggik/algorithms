import sys
input = sys.stdin.readline
n,m = map(int, input().split())
num = list(map(int, input().split()))
summ = [0]*(n+1)
val = 0
for i in range(n):
    val += num[i]
    summ[i+1] = val
for _ in range(m):
    a,b = map(int, input().split())
    print(summ[b]-summ[a-1])