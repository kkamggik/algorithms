def solution(n, arr1, arr2):
    answer = [[' ']*n for _ in range(n)]
    for i in range(n):
        s = bin(arr1[i])[2:]
        if len(s) < n:
            s = '0'*(n-len(s))+s
        for j in range(n):
            if s[j]=='1':
                answer[i][j] = '#'
    for i in range(n):
        s = bin(arr2[i])[2:]
        if len(s) < n:
            s = '0'*(n-len(s))+s
        for j in range(n):
            if s[j]=='1':
                answer[i][j] = '#'
    rst = []
    for ans in answer:
        rst.append(''.join(ans))
    return rst
