diff = 0
answer = []
Apeach = []
Ryan = [0]*11
def difference():
    rst = 0
    for i in range(11):
        if Apeach[i] == 0 and Ryan[i]==0: continue
        if Apeach[i] < Ryan[i]: rst += 10-i
        else: rst -= 10-i
    return rst
def dfs(idx,left):
    if idx==-1 and left: return
    if left == 0:
        global diff, answer
        rst = difference()
        if rst > diff:
            diff = rst
            answer = Ryan[:]
        return
    for i in range(left, -1, -1):
        Ryan[idx] = i
        dfs(idx-1, left-i)
        Ryan[idx] = 0

def solution(n, info):
    global diff, answer, Apeach
    answer = []
    Apeach = info[:]
    Ryan = []
    dfs(10,n)
    return answer
print(solution(	10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))