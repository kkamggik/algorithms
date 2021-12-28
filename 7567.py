s = input()
stack = []
ans = 0
for i in s:
    if not stack: ans += 10
    elif stack[-1]=='(':
        if i==')': ans+=10
        else: ans+=5
    elif stack[-1]==')':
        if i==')': ans += 5
        else: ans += 10
    stack.append(i)
print(ans)
