def solution(n):
    answer = 0
    for i in range(1,(n//2)+1):
        now = i
        for j in range(i+1,n):
            now += j
            if now == n: 
                answer += 1
                break
            elif now > n: break
    return answer+1
print(solution(1))