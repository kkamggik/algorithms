a,b = map(int, input().split())
curr = 1
s = 0
val = 1
cnt = 1
while curr <= b:
    if curr >= a:
        s += val
    if cnt == val:
        cnt = 0
        val += 1
    curr += 1
    cnt += 1
print(s)

