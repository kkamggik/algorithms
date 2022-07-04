def calculate(a,b,ans):
    for i in range(0, len(a)-len(b)+1):
        rst  = 0
        for j in range(len(b)):
            rst += (a[i+j]*b[j])
        ans = max(ans, rst)
    return ans
T = int(input())
for test_case in range(1, T + 1):
    n, m  =  map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rst = -1e9
    if len(a) >= len(b):
        print("#{} {}".format(test_case,calculate(a,b, rst)))
    else:
        print("#{} {}".format(test_case,calculate(b,a, rst)))