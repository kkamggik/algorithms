import sys
input = sys.stdin.readline
n,m = map(int, input().split())
dic = {}
for _ in range(n):
    name = input()
    dic[name] = True
ans = []
for _ in range(m):
    name = input()
    if name in dic: ans.append(name)
ans.sort()
print(len(ans))
for i in ans: print(i)