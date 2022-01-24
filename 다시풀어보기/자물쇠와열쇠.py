nlock = []
nkey = []
def check():
    n = len(nlock)//3
    for i in range(n,2*n):
        for j in range(n,2*n):
            if nlock[i][j]!=1: return False
    return True
def rotate(key):
    global nkey
    nkey = [[key[j][i] for j in range(len(key))] for i in range(len(key[0])-1,-1,-1)]
def new_lock(lock,n):
    global nlock
    m = len(lock[0])+3*llen
    for i in range(n): nlock.append([0]*m)
    for i in range(len(lock)): nlock.append([0]*llen+lock[i]+[0]*llen)
    for i in range(n): nlock.append([0]*m)
def solution(key, lock):
    global nkey
    klen = len(key)
    llen = len(lock)
    new_lock(lock,llen)
    nkey = key[:]
    n,m = len(nlock), len(nlock[0])
    for i in range(llen*2):
        for j in range(llen*2):
            for d in range(4):
                rotate(nkey)
                for ii in range(klen):
                    for jj in range(klen):
                        nlock[ii+i][jj+j] += nkey[ii][jj]
                if check()==True: return True
                for ii in range(klen):
                    for jj in range(klen):
                        nlock[ii+i][jj+j] -= nkey[ii][jj]
    return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))