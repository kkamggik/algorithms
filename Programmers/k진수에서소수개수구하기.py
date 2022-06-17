def is_prime_number(x):
    if x <= 1: return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False 
    return True
def convert(n,k):
    res = ''
    while n!=0:
        n,mod = divmod(n,k)
        res += str(mod)
    return res[::-1]
def solution(n, k):
    answer = 0
    n = convert(n,k)
    idx = 0
    num = ''
    while idx < len(n):
        if n[idx]!='0':
            num += n[idx]
        else:
            if num and is_prime_number(int(num))==True:
                answer += 1
            num = ''
        idx += 1
    if num and is_prime_number(int(num))==True:
        answer += 1
    return answer