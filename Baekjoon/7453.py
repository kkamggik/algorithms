n = int(input())
alist, blist, clist, dlist = [],[],[],[]
for _ in range(n):
    a,b,c,d = map(int, input().split())
    alist.append(a)
    blist.append(b)
    clist.append(c)
    dlist.append(d)
ab = {}
for a in alist:
    for b in blist:
        if a+b not in ab:
            ab[a+b] = 1
        else:
            ab[a+b] += 1
ans = 0
for c in clist:
    for d in dlist:
        if -(c+d) in ab:
            ans += ab[-(c+d)]
print(ans)
