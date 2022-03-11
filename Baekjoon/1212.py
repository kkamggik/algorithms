n = input()
rst = ''
for i in range(len(n)):
    t = int(n[i])
    tmp = ''
    while t!=0:
        tmp += str(t%2)
        t //= 2
    if i!=0:
        while len(tmp) < 3:
            tmp = tmp+"0"
    rst += tmp[::-1]
if not rst: print(0)
else: print(rst)