import sys
input = sys.stdin.readline
n = int(input())
s = input().strip()
red,blue = 0,0
cnt1,cnt2,cnt3,cnt4 = 0,0,0,0
for i in s:
    if i == 'R':
        red += 1
        cnt2 += blue
        blue = 0
    else:
        blue += 1
        cnt1 += red
        red = 0
red,blue = 0,0
for i in s[::-1]:
    if i == 'R':
        red += 1
        cnt3 += blue
        blue = 0
    else:
        blue += 1
        cnt4 += red
        red = 0
print(min(cnt1, cnt2, cnt3, cnt4))