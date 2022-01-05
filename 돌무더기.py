from copy import deepcopy
answer = ''
def tracking(stones,idx,k,n,ans):
    for i in range(n):
        if i == idx: stones[i] += 1
        else: stones[i] -= 1
        if stones[i] == -1:
             return
    if stones.count(0) == n-1:
        if max(stones) == k: 
            global answer
            answer = max(answer, ans)
        return
    for i in range(n-1,-1,-1):
        tstones = deepcopy(stones)
        tracking(tstones,i,k,n,ans+str(i))
def solution(stones, k):
    n = len(stones)
    temp = deepcopy(stones)
    for i in range(n-1,-1,-1):
        stones = deepcopy(temp)
        tracking(stones,i,k,n,str(i))
    if answer=='': return '-1'
    else: return answer