import sys
input = sys.stdin.readline
n= int(input())
stack = [0]
curr = 1
ans = []
arr = [int(input()) for _ in range(n)]
for t in arr:
    if stack and t < stack[-1]:
        ans = 'NO'
        break
    while t > stack[-1]:
        stack.append(curr)
        ans.append('+')
        curr += 1
    while t <= stack[-1]:
        stack.pop()
        ans.append('-')
if ans == 'NO': print(ans)
else:
    for op in ans: print(op)