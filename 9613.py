import sys
input = sys.stdin.readline
def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    s = 0
    for i in range(n):
        for j in range(i+1,n):
            s += gcd(arr[i],arr[j])
    print(s)

