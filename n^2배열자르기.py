def solution(n, left, right):
    answer = []
    r1,c1 = left//n, left%n
    r2,c2 = right//n, right%n
    arr = []
    if r1==r2:
        c = r1+1
        m = right-left+1
        for i in range(n):
            if i < c1 or i > c2: continue
            if i < c: arr.append(c)
            else: arr.append(i+1)
    else:
        for i in range(r1, r2+1):
            c = i+1
            if i == r1: s,e = c1,n
            elif i == r2: s,e = 0,c2
            else: s,e = 0,n
            for j in range(n):
                if j < s or j > e: continue
                if j < c: arr.append(c)
                else: arr.append(j+1)
    return arr
print(solution(5, 0, 4))