import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
answer = 0
for i in range(1,n+1):
    answer = max(answer, i*arr[i-1])
print(answer)
