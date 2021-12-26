test = int(input())
for _ in range(test):
    n = int(input())
    zero, one = 1,0
    for i in range(n):
        tmp = one
        one += zero
        zero = tmp
    print(zero, one)