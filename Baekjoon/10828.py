import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    cmlist = list(map(str, sys.stdin.readline().split()))
    if cmlist[0] == 'push':
        stack.append(cmlist[1])
    elif cmlist[0] == 'pop':
        x = -1
        if stack:
            x = stack[-1]
            stack.pop()
        print(x)
    elif cmlist[0] == 'size':
        print(len(stack))
    elif cmlist[0] == 'empty':
        if stack: print(0)
        else: print(1)
    elif cmlist[0] == 'top':
        x = -1
        if stack:
            x = stack[-1]
        print(x)