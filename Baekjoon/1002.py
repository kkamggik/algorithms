# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
# 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
# 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
import math
t = int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dist==0 and r1==r2: print(-1)
    elif abs(r1-r2)==dist or r1+r2==dist: print(1)
    elif abs(r1-r2)< dist < (r1+r2): print(2)
    else: print(0)
