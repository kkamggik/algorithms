import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
answer = [0]*n
arr = arr[::-1]
stack = [0]
for i in range(1,n):
    while stack and arr[stack[-1]] < arr[i]:
        x = stack.pop()
        answer[x] = n-i
    stack.append(i)
for i in range(n-1,-1,-1):
    print(answer[i],end=' ')