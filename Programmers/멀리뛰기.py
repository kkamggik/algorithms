def solution(n):
    if n <= 3: return n
    n1,n2 = 2,3
    for i in range(4,n+1):
        answer = (n1+n2)%1234567
        n1,n2 = n2,answer
    return answer