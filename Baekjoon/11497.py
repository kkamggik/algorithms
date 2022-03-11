import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 0
    stack = []
    for i in range(0,n,2):
        stack.append(arr[i])
    if n%2==0:
        for i in range(n-1,-1,-2):
            stack.append(arr[i])
    else:
        for i in range(n-2, -1,-2):
            stack.append(arr[i])
    for i in range(n):
        answer = max(answer, abs(stack[i-1]-stack[i]))
    print(answer)
