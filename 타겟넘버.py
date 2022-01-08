answer = 0 
def dfs(idx, numbers, target, s):
    global answer
    if idx==len(numbers):
        if target==s: answer += 1
        return
    dfs(idx+1, numbers, target, s+numbers[idx])
    dfs(idx+1, numbers, target, s-numbers[idx])
def solution(numbers, target):
    dfs(0, numbers, target, 0)
    return answer
print(solution([1,1,1,1,1],3))