import sys
input = sys.stdin.readline
n,k,b = map(int, input().split())
lights = [1]*(n+1)
for _ in range(b):
    lights[int(input())] = 0
cnt = 0
answer = 0
for i in range(1,k+1):
    if lights[i] == 0: cnt += 1
left, right = 1, k+1
answer = cnt
while right <= n:
    if lights[right] == 0: cnt += 1
    right += 1
    if lights[left] == 0: cnt -= 1
    left += 1
    answer = min(answer, cnt)
print(answer)
