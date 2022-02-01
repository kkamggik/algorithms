import sys
input = sys.stdin.readline
n,m = map(int, input().split())
namecnt = [0]*21
names = [0]*n
answer = 0
for i in range(n):
    name = len(input().strip())
    names[i] = name
    if i > m:
        namecnt[names[i-m-1]] -= 1
    answer += namecnt[name]
    namecnt[name] += 1
print(answer)

