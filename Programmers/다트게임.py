def solution(dartResult):
    answer = 0
    stack = []
    score = {'S':1, 'D':2, 'T':3}
    dartResult = dartResult.replace("10","N")
    for i in dartResult:
        if i.isdigit() or i=='N':
            stack.append(10 if i=='N' else int(i))
        elif i in ['S','D','T']:
            num = stack.pop()
            stack.append(num**score[i])
        elif i == '#':
            stack[-1] *= -1
        elif i == '*':
            stack[-1] *= 2
            if len(stack)>=2:
                stack[-2] *= 2
    return sum(stack)
print(solution("1D2S#10S"))