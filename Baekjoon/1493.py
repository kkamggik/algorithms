length, width, height = map(int, input().split())
n = int(input())
cubes = []
for _ in range(n):
    a,b = map(int, input().split())
    cubes.append([a, b])
cubes.sort(reverse=True)
before = 0
ans = 0
for w,cnt in cubes:
    before <<= 3
    v = 2**w
    maxcnt = (length//v)*(width//v)*(height//v) - before
    maxcnt = min(cnt, maxcnt)
    ans += maxcnt
    before += maxcnt
if before == length*height*width: print(ans)
else: print(-1)
 