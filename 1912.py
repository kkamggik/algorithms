import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
s = [arr[0]]
for i in range(n-1):
    s.append(max(s[i]+arr[i+1], arr[i+1]))
print(max(s))