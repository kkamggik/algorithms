import sys
input = sys.stdin.readline
n,m = map(int, input().split())
string = []
minpack, minind = 1e9,1e9
for _ in range(m):
    a,b = map(int, input().split())
    if b*6 < a: a = b*6
    minpack = min(minpack, a)
    minind = min(minind, b)
pack = n//6
ind = n%6
answer = pack*minpack + ind*minind
if ind > 0:
    answer = min(answer, (pack+1)*minpack)
print(answer)