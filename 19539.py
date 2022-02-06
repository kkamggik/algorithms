import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
summ = sum(arr)
turn = summ//3
if summ%3 != 0:
    print('NO')
else:
    for a in arr:
        turn -= a//2
    if turn > 0: print('NO')
    else: print('YES')