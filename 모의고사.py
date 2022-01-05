def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    answer = [0,0,0]
    fs,ss,ts = 0,0,0
    for a in range(len(answers)):
        if answers[a] == first[a%len(first)]: fs+=1
        if answers[a] == second[a%len(second)]: ss+=1
        if answers[a] == third[a%len(third)]: ts+=1
    answer = []
    m = max(fs,ss,ts)
    if fs == m: answer.append(1)
    if ss == m: answer.append(2)
    if ts == m: answer.append(3)
    return answer
print(solution([1,3,2,4,2]))