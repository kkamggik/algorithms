import sys
input = sys.stdin.readline
n, atk = map(int, input().split())
maps = []
maxhp, maxatk, monster = 0,0,0
for _ in range(n):
    t,a,h = map(int, input().split())
    maps.append([t,a,h])
    if t == 1:
        maxhp = max(maxhp, h)
        maxatk = max(maxatk, a)
        monster += 1
left, right = 1, maxhp*maxatk*monster
while left <= right:
    mid = (left + right)//2 # mid는 HmaxHP임..
    attack = atk
    currHP = mid
    flag = True
    for t,a,h in maps:
        if t == 1:
            attacks = h//attack
            if h%attack == 0: attacks -= 1
            if attacks > 0: currHP -= attacks*a
            if currHP <= 0:
                flag = False
                break
        else:
            attack += a
            currHP += h
            if currHP > mid: currHP = mid
    if flag == False:
        left = mid+1
    else:
        right = mid-1
print(left)
            
    
