import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
answer = [-1]*n
stack = [0]
for i in range(1,n):
    while stack and arr[i] > arr[stack[-1]]:
        x = stack.pop()
        answer[x] = arr[i]
    stack.append(i)
print(answer)