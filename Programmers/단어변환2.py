answer = 2e9
arr = []
visited = []
target_word = ""
def convert(begin, cnt):
    if(begin == target_word):
        global answer
        answer = min(answer, cnt)
    for i in range(len(arr)):
        if(visited[i]): continue
        diff = 0
        for j in range(len(begin)):
            if(begin[j]!=arr[i][j]): diff += 1
        if(diff == 1):
            visited[i] = 1
            convert(arr[i], cnt+1)
            visited[i] = 0
def solution(begin, target, words):
    if target not in words: return 0
    global arr, visited, target_word
    arr = words[:]
    target_word = target
    visited = [0]*(len(words))
    convert(begin, 0)
    return answer