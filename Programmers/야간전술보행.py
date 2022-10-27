def solution(distance, scope, times):
    answer = [0]*(distance+1)
    n = len(scope)
    for i in range(n):
        t = times[i][0] + times[i][1]
        start = ((scope[i][0]//t) * t) + 1
        curr = 1
        for j in range(start, scope[i][1]+1):
            if(scope[i][0] <= j and curr <= times[i][0]):
                answer[j] = 1
            curr += 1
            if(curr > t): curr = 1
    for i in range(1, distance+1):
        if(answer[i]): return i
    return distance

print(solution(	10, [[5, 10]], [[0, 5]]))