answer = 0
lst = []
info = []
def dfs(sheep, wolf, nxt):
    global answer
    answer = max(answer, sheep)
    for curr_node in nxt:
        for next_node in lst[curr_node]:
            if next_node not in nxt:
                nsheep = sheep
                nwolf = wolf
                if info[next_node]==1: nwolf+=1
                else: nsheep += 1
                if nwolf >= nsheep: continue
                dfs(nsheep,nwolf,nxt+[next_node])
            
def solution(infos, edges):
    global lst,info
    info = infos[:]
    lst = [[] for _ in range(len(info))]
    for a,b in edges:
        lst[a].append(b)
        lst[b].append(a)
    dfs(1,0,[0])
    return answer