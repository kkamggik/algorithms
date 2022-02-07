n = int(input())
arr = [list(input()) for _ in range(n)]
answer = n*n+1
for bit in range(1<<n): #only row만 뒤집는 모든 경우의 수 구하긔
    temp = [arr[_][:] for _ in range(n)] # 복사하긩
    for i in range(n):
        if bit & (1<<i):
            for j in range(n):
                if temp[i][j] == 'H':
                    temp[i][j] = 'T'
                else:
                    temp[i][j] = 'H'
    rst = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if temp[j][i] == 'T': cnt += 1
        rst += min(cnt, n-cnt)
    answer = min(answer, rst)
print(answer)