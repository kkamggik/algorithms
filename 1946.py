import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    candidates = []
    for i in range(n):
        a,b = map(int, input().split())
        candidates.append([a,b])
    candidates.sort()
    score = candidates[0][1]
    answer = 1
    for i in range(1,n):
        if candidates[i][1] < score:
            answer += 1
            score = candidates[i][1]
    print(answer)