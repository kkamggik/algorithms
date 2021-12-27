from collections import deque
def check(s):
    queue = deque()
    for i in s:
        if i==')':
            if queue and queue[-1]=='(':
                queue.pop()
            else:
                return 'no'
        elif i=='(':
            queue.append(i)
        elif i=='[':
            queue.append(i)
        elif i==']':
            if queue and queue[-1]=='[':
                queue.pop()
            else:
                return 'no'
    if not queue: return 'yes'
    return 'no'
s = ''
while True:
    t = input()
    if t=='.': break
    if '.' in t:
        s += t
        print(check(s))
        s = ''
    else:
        s += t
