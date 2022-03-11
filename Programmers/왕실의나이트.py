dirc = [[2,-1],[2,1],[-2,1],[-2,-1],[-1,2],[1,2],[-1,-2],[1,-2]]
loc = input()
x = ord(loc[0]) - ord('a')
y = int(loc[1]) - 1
ans = 0
for d in dirc:
    nx,ny = x+d[0],y+d[1]
    if 0<=nx<8 and 0<=ny<8:
        ans += 1
print(ans)
