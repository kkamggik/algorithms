n = int(input())
s = input().strip()
stack = []
idx = 0
while idx < n:
    stack.append('*')
    if s[idx]=='L': idx += 1
    idx += 1
stack.append('*')
print(min(n, len(stack)))


