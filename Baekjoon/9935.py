from collections import deque
s = input()
b = list(input())
stack = []
for i in s:
    stack.append(i)
    if len(stack) >= len(b) and stack[-len(b):]==b:
        del stack[-len(b):]
if not stack: print('FRULA')
else: print(''.join(stack))        

