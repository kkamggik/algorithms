import sys
input = sys.stdin.readline
a,b = map(int, input().split())
n = int(input())
arr = [int(input()) for _ in range(n)]
answer = abs(a-b)
for i in arr:
    answer = min(answer, abs(i-b)+1)
print(answer)