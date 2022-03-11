n = int(input())
for _ in range(n):
    s = input()
    rst = 0
    cnt = 0
    for i in s:
        if i=='O':
            cnt += 1
        else:
            cnt = 0
        rst += cnt
    print(rst)