def solution(brown, yellow):
    answer = []
    for i in range(3,(5000//3)+1):
        for j in range(3,(5000//3)+1):
            if i*j == brown+yellow:
                if yellow == (i-2)*(j-2) or yellow == (j-2)*(i-2):
                    return [j,i]
            elif i*j > brown+yellow: break
    return answer
print(solution(24,24))