def count(n):
    cnt = 0
    for i in range(1,n+1): cnt += i
    return cnt
def solution(n):
    # down up right
    answer = [[0]*n for _ in range(n)]
    answer[0][0] = 1
    idx = 2
    dirc = 0
    x,y = 0,0
    total = count(n)
    end = n
    while idx <= total:
        if dirc == 0:
            y += 1
            if y >= n or answer[y][x]!=0:
                dirc = 2
                x,y = x+1,y-1
        elif dirc == 1:
            x,y = x-1,y-1
            if answer[y][x]!=0:
                x += 1
                y += 2
                dirc = 0
        elif dirc == 2:
            x += 1
            if x >= end or answer[y][x]!=0:
                dirc = 1
                x -= 2
                y -= 1
                end -= 1
        answer[y][x] = idx   
        idx += 1
    rst = []
    for i in range(n):
        for j in range(i+1):
            rst.append(answer[i][j])
    return rst
print(solution(6))