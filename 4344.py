import sys
input = sys.stdin.readline
tests = int(input())
for t in range(tests):
    lst = list(map(int, input().split()))
    n = lst[0]
    lst = lst[1:]
    avg = sum(lst)/n
    cnt = 0
    for i in lst:
        if i > avg: cnt+=1
    num = (cnt/n)*100
    print('{:.3f}%'.format(num))