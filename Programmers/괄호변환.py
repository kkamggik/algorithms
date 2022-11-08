def correct(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append('(')
        else:
            if not stack: return False
            stack.pop()
    if stack: return False
    return True

def balanced(p):
    left, right = 0, 0
    for i in range(len(p)):
        if(p[i] == '('): left += 1
        else: right += 1
        if(left == right): return [p[:i+1], p[i+1:]]

def recursion(p):
    if not p: return ''
    u,v = balanced(p)
    if(correct(u)):
        u += recursion(v)
        return u
    else:
        t = '('
        t += recursion(v)
        t += ')'
        u = u[1:-1]
        for c in u:
            if(c=='('): t += ')'
            else: t += '('
        return t
    
def solution(p):
    if not p: return ''
    if correct(p): return p
    answer = recursion(p)
    return answer
print(solution(")("))