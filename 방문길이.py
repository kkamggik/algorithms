def solution(dirs):
    answer = 0
    dic = {}
    x,y = 0,0
    for d in dirs:
        nx,ny = x,y
        if d == 'U' and y-1 >= -5: ny -= 1
        elif d == 'D' and y+1 <= 5: ny += 1
        elif d == 'L' and x-1 >= -5: nx -= 1
        elif d == 'R' and x+1 <= 5: nx += 1
        if x==nx and y==ny: continue
        t1 = str(x)+','+str(y)+','+str(nx)+','+str(ny)
        t2 = str(nx)+','+str(ny)+','+str(x)+','+str(y)
        if t1 not in dic and t2 not in dic:
            dic[t1] = 1
            dic[t2] = 1
            answer += 1
        else:
            dic[t1] = 1
            dic[t2] = 1
        x,y = nx,ny
    return answer
print(solution("LULLLLLLU"))