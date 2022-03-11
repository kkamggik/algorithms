def d(n):
    rst = int(n)
    for i in n:
        rst += int(i)
    return rst
num = [True]*10001
for i in range(1, 10001):
    if num[i] == False: continue
    rst = d(str(i))
    while rst <= 10000 and num[rst]==True:
        num[rst] = False
        rst = d(str(rst))
for i in range(1,10001):
    if num[i]==True:
        print(i)