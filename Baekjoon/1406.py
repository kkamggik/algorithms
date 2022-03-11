import sys
input = sys.stdin.readline
left, right = list(input().strip()),[]
n = int(input())
for _ in range(n):
    cm = input().split()
    if cm[0]=='L':
        if left: right.append(left.pop())
    elif cm[0] == 'D':
        if right: left.append(right.pop())
    elif cm[0] == 'P':
        left.append(cm[1])
    elif cm[0] == 'B':
        if left: left.pop()
arr = left + right[::-1]
print(''.join(arr))
