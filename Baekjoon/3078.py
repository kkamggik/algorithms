import sys
input = sys.stdin.readline
n,m = map(int, input().split())
names = []
for _ in range(n):
    name = input().strip()
    names.append(len(name))
answer = 0
namelen = [0]*21
left, right = 0,0
while left < n-1:
    if right < n:
        namelen[names[right]] += 1
        right += 1
    if right > m or right==n:
        name = names[left]
        namelen[names[left]] -= 1
        answer += namelen[names[left]]
        left += 1
print(answer)