def calculate(a,b):
    if b%2 == 1: return calculate(a,b-1)*a
    elif b == 0: return 1
    elif b == 1: return a
    else:
        result = calculate(a,b//2)%c
        return result*result
a,b,c = map(int, input().split())
print(calculate(a,b)%c)