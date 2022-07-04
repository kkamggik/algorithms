T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rst = [[] for _ in range(n)]
    for i in range(n):
        t = ''
        for j in range(n-1,-1,-1):
            t += str(arr[j][i])
        rst[i].append(t)
    idx = 0
    for i in range(n-1,-1,-1):
        t = ''
        for j in range(n-1,-1,-1):
            t += str(arr[i][j])
        rst[idx].append(t)
        idx += 1
    idx = 0
    for i in range(n-1,-1,-1):
        t = ''
        for j in range(n):
            t += str(arr[j][i])
        rst[idx].append(t)
        idx += 1
    print("#{}".format(test_case))
    for row in rst:
        print(' '.join(row))
