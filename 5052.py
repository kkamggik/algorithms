import sys
input = sys.stdin.readline
def check():
    for i in range(len(num)-1):
        if num[i] in num[i+1]:
            return 'NO'
    return 'YES'
t = int(input())
for _ in range(t):
    num = []
    n = int(input())
    for i in range(n):
        t = input().strip()
        num.append(t)
    num.sort()
    print(check())