import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
answer = abs(n-100)
if m!=0: broken = set(input().split())
else: broken = set()
for i in range(1000001):
    for num in str(i):
        if num in broken: break
    else:
        answer = min(answer, len(str(i)) + abs(i-n))
print(answer)