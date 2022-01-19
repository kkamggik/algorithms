def solution(s):
    answer = -1
    stack = []
    for i in s:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    if not stack: return 1
    return 0
print(solution('baabaa'))