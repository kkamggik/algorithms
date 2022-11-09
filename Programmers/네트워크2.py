networks = []
arr = []
def dfs(idx):
    for i in range(len(networks)):
        if(networks[i] == 0 and arr[idx][i] == 1):
            networks[i] = 1
            dfs(i)
            
def solution(n, computers):
    answer = 0
    global networks, arr
    networks = [0]*n
    arr = computers[:]
    cnt = 0
    for i in range(n):
        if(networks[i] == 0):
            networks[i] = 1
            dfs(i)
            cnt += 1
    return cnt