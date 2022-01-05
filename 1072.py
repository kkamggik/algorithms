x,y = map(int, input().split())
z = (y*100)//x
left,right = 0,1000000000
if z >= 99: print(-1)
else:
    while left <= right:
        mid = (left+right)//2
        tx,ty = x+mid, y+mid
        p = (ty*100)//tx
        if p > z: 
            answer = mid
            right = mid -1
        else: left = mid+1
    print(answer)