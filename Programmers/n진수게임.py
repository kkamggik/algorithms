def convert(n,q):
    num = ''
    while n > 0:
        if n%q < 10:
            num += str(n%q)
        else:
            num += chr(n%q-10+65)
        n //= q
    if num=='': return '0'
    return num[::-1]
def solution(n,t,m,p):
    cnt = 0
    num = 0
    ans = ''
    turn = 1
    while cnt < t:
        s = convert(num,n)
        for i in s:
            if turn == p and cnt < t:
                ans += i
                cnt += 1
            turn += 1
            if turn > m:
                turn = 1
        num += 1
    return ans
print(solution(2,4,2,1))    
print(solution(16,16,2,1))    