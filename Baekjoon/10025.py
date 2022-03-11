import sys
input = sys.stdin.readline
n,k = map(int, input().split())
maxdist = 0
ice = [0]*1000001
for _ in range(n):
    g,x = map(int, input().split())
    ice[x] = g
    maxdist = max(maxdist, x)
summ = 0
for i in range(k*2+1):
    if i > maxdist: break
    summ += ice[i]
answer = summ
left, right = 0, k*2+1
while right <= maxdist:
    summ += ice[right]
    right += 1
    summ -= ice[left]
    left += 1
    answer = max(answer, summ)
print(answer)
