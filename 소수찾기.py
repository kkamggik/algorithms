from itertools import permutations
def isPrime(n):
    if n==0 or n==1: return False
    for i in range(2,n):
        if n%i == 0: return False
    return True
def solution(numbers):
    nums = list(numbers)
    answer = 0
    s = set()
    for i in range(1, len(nums)+1):
        perm = permutations(nums, i)
        for p in perm:
            n = ''
            for j in p:
                n += j
            s.add(int(n))
    for n in s:
        if isPrime(n): answer += 1
    return answer
print(solution("17"))