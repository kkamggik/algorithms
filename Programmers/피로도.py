answer = 0
n = 0
visited = [0]*8
dungeon = []
def dfs(left, cnt):
    global answer 
    answer = max(cnt, answer)
    for i in range(n):
        if (left >= dungeon[i][0] and visited[i] == 0):
            visited[i] = 1
            dfs(left - dungeon[i][1], cnt+1)
            visited[i] = 0
def solution(k, dungeons):
    global n, dungeon
    n = len(dungeons)
    dungeon = dungeons[:]
    dfs(k, 0)
    return answer