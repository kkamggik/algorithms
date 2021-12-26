import sys
input = sys.stdin.readline
dic = {}
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
src = list(map(int, input().split()))
for i in range(n):
    dic[arr[i]] = True
for i in range(m):
    if src[i] in dic:
        print(1)
    else:
        print(0)
