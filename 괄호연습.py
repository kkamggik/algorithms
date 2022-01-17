def balanced(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append('(')
        else:
            if not stack: return False
            stack.pop()
    if stack: return False
    return True
def split(p):
    opened = 0
    closed = 0
    for i in range(len(p)):
        if p[i] == '(': opened += 1
        else: closed += 1
        if opened == closed: return [p[:i+1],p[i+1:]]
def recursion(p):
    if p == '': return p
    u,v = split(p)
    if balanced(u):
        u += recursion(v)
        return u
    else:
        t = '('
        t += recursion(v)
        t += ')'
        u = u[1:-1]
        for i in u:
            if i=='(': t+=')'
            else: t+='('
        return t
def solution(p):
    if p == '': return ''
    if balanced(p): return p
    answer = recursion(p)
    return answer
print(solution("()))((()"))