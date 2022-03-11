import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().strip()))
stack = []
size = n-m
for num in arr:
    while m > 0 and stack and stack[-1] < num:
        stack.pop()
        m -= 1
    stack.append(num)
for i in range(size): print(stack[i],end='')