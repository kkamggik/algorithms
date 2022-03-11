import math
def is_prime_number(x):
    if x == 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True # 소수임
def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
def solution(n, k):
    answer = 0
    s = str(convert(n,k))
    string = s.split('0')
    for s in string:
        if s == '': continue
        if is_prime_number(int(s)): answer += 1
    return answer