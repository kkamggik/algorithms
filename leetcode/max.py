def max3(a,b,c):
    if a > b: a,b = b,a
    if b > c: b,c = c,b
    print(a,b,c)
    return c
A = int(input('A = '))
B = int(input('B = '))
C = int(input('C = '))
res = max3(A,B,C)
print('최대값: ',res)