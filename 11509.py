import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arrows = [0]*1000001
answer = 0
for a in arr:
    if arrows[a] > 0:
        arrows[a] -= 1
        arrows[a-1] += 1
    else:
        answer += 1
        arrows[a-1] += 1
print(answer)