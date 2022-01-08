answer = 1e9
def convert(before, after):
    cnt = 0
    for i in range(len(before)):
        if before[i] != after[i]:
            cnt += 1
        if cnt > 1: return False
    return True

def dfs(visited, target, idx, cnt, words):
    if words[idx] == target: 
        global answer
        answer = min(answer, cnt)
        return
    if cnt == len(visited):
        return 
    for i in range(len(visited)):
        if visited[i] == False and convert(words[idx], words[i])==True:
            visited[i] = True
            dfs(visited, target, i, cnt+1, words)
            visited[i] = False

    
def solution(begin, target, words):
    if target not in words: return 0
    visited = [False]*len(words)
    for i in range(len(words)):
        if convert(words[i], begin):
            visited[i] = True
            dfs(visited, target, i, 1, words)
            visited[i] = False
    return answer
print(solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))