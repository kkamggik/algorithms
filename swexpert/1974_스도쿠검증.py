T = int(input())
def check(arr):
    row = [0]*10
    col = [0]*10
    nums = [0]*10
    for i in range(9):
        #가로
        for j in range(9):
            row[arr[i][j]] += 1
            col[arr[j][i]] += 1
        if row[1:].count(0) >= 1: return 0
        if col[1:].count(0) >= 1: return 0
        for j in range(10):
            col[j] = 0
            row[j] = 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            for y in range(i,i+3):
                for x in range(j,j+3):
                    nums[arr[y][x]] += 1
            if nums[1:].count(0) >= 1: return 0
            for c in range(10): nums[c] = 0
    return 1
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    rst = check(arr)
    print("#{} {}".format(test_case, rst))