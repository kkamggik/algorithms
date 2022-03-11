def factorial(x):
    if fact[x]!=0:
        return fact[x]
    fact[x] = x*factorial(x-1)
    return fact[x]
fact = [0]*501
fact[0] = 1
fact[1] = 1
fact[2] = 2
n = int(input())
factorial(n)
x = str(fact[n])
cnt = 0
for i in x[::-1]:
    if i == '0': cnt+=1
    else: break
print(cnt)