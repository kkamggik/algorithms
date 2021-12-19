from copy import deepcopy
def rotate(key,n):
    nkey = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nkey[j][n-i-1] = key[i][j]
    return nkey
def check(lock):
    l = len(lock)//3
    for i in range(l,l*2):
        for j in range(l,l*2):
            if lock[i][j] != 1:
                return False
    return True
def solution(key, lock):
    n = len(lock)
    m = len(key)
    # lock의 새로운 배열 만들기
    new = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new[i+n][j+n] = lock[i][j]
    for r in range(4):
        key = rotate(key,m)
        for y in range(n*2):
            for x in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new[y+i][x+j] += key[i][j]
                if check(new)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new[y+i][x+j] -= key[i][j]
    return False
print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))