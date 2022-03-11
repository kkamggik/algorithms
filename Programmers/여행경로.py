answer = []
def dfs(visited,idx,last,cnt,tickets):
    if cnt == len(visited):
        global answer
        tans = ['']*(cnt+1)
        for v in range(cnt):
            tans[visited[v]] = tickets[v][0]
            if visited[v] == cnt-1:
                tans[-1] = tickets[v][1]
        flag = False
        for v in range(cnt+1):
            if answer[v] > tans[v]:
                flag = True
                break
            elif answer[v] < tans[v]: break
        if flag:
            for v in range(cnt+1):
                answer[v] = tans[v]
        return
    for i in range(len(visited)):
        if visited[i] == -1 and tickets[i][0]==last:
            visited[i] = cnt
            dfs(visited, i, tickets[i][1], cnt+1, tickets)
            visited[i] = -1
        
def solution(tickets):
    global answer
    answer = ['zzz']*(len(tickets)+1)
    visited = [-1]*len(tickets)
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visited[i] = 0
            dfs(visited, i, tickets[i][1], 1, tickets)
            visited[i] = -1
    return answer
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))