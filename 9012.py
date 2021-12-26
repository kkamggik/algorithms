def check(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if not stack: return 'NO'
            elif stack[-1] == '(':
                stack.pop()
            else: return 'NO'
    if not stack: return 'YES'
    else: return 'NO'
n = int(input())
for _ in range(n):
    s = input()
    print(check(s))