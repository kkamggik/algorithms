import sys
input = sys.stdin.readline
n = int(input())
dic = set()
for _ in range(n):
    t = input().strip()
    dic.add(t)
lst = list(dic)
lst.sort()
lst.sort(key = len)
for word in lst: print(word)