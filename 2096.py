import sys
input = sys.stdin.readline
n = int(input())
maxarr = [0]*3
minarr = [0]*3
maxcurr = [0]*3
mincurr = [0]*3
for i in range(n):
    a,b,c = map(int, input().split())
    for j in range(3):
        if j==0:
            maxcurr[j] = max(maxarr[j], maxarr[j+1]) + a
            mincurr[j] = min(minarr[j], minarr[j+1]) + a
        elif j == 2:
            maxcurr[j] = max(maxarr[j], maxarr[j-1]) + c
            mincurr[j] = min(minarr[j], minarr[j-1]) + c
        else:
            maxcurr[j] = max(maxarr[j], maxarr[j+1], maxarr[j-1]) + b
            mincurr[j] = min(minarr[j], minarr[j+1], minarr[j-1]) + b
    for j in range(3):
        maxarr[j] = maxcurr[j]
        minarr[j] = mincurr[j]
print(max(maxarr), min(minarr))