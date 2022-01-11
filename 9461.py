t = int(input())
s = [1,1,1]
for i in range(3,101):
    s.append(s[i-2]+s[i-3])
print(s)
for _ in range(t):
    n = int(input())
    print(s[n-1])