import sys
input = sys.stdin.readline
n = int(input())
neg, pos = [],[]
one = 0
for _ in range(n):
    x = int(input())
    if x == 1: one += 1
    elif x > 0: pos.append(x)
    else: neg.append(x)
pos.sort(reverse=True)
neg.sort()
answer = 0
for i in range(0, len(pos), 2):
    if i+1 < len(pos):
        answer += pos[i]*pos[i+1]
    else:
        answer += pos[i]
for i in range(0, len(neg), 2):
    if i+1 < len(neg):
        answer += neg[i] * neg[i+1]
    else:
        answer += neg[i]
answer += one
print(answer) 
