def solution(n,a,b):
    answer = 1
    idx = 2
    flag = False
    while idx < n:
        for i in range(0,n,idx):
            s,e = i,i+idx
            if s<a<=e and s<b<=e: flag = True
        if flag == True: return answer
        idx*=2
        answer += 1
    return answer
print(solution(8,4,7))