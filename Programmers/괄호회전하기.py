from collections import deque
def check(s):
    stack = []
    for i in s:
        if i in ['(','[','{']:
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1]!='(': return False
            stack.pop()
        elif i == ']':
            if not stack or stack[-1]!='[': return False
            stack.pop()
        elif i == '}':
            if not stack or stack[-1]!='{': return False
            stack.pop()
    if stack: return False
    return True
def solution(s):
    answer = 0
    queue = deque()
    s = list(s)
    queue = deque(s)
    for i in range(len(s)):
        x = queue.popleft()
        queue.append(x)
        if check(queue)==True: answer += 1
    return answer