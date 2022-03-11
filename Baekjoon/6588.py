prime = [True]*1000001
prime[0] = False
prime[1] = False
for i in range(2,1000001):
    if prime[i] == True:
        for j in range(i+i, 1000001, i):
            prime[j] = False
while True:
    num = int(input())
    if num==0: break
    for i in range(3,num):
        if prime[i]==True and prime[num-i]==True:
            a,b = i,num-i
            print("{} = {} + {}".format(num, a, b))
            break