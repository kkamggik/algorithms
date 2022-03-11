n = int(input())
if n!=1:
    prime = 2
    while n!=1:
        if n%prime==0:
            print(prime)
            n//=prime
        else: prime += 1