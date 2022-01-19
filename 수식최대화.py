from itertools import permutations
def calculate(idx,op,exp):
    if exp.isdigit(): return str(exp)
    if op[idx] == '*':
        exps = exp.split('*')
        tmp = []
        for e in exps:
            tmp.append(calculate(idx+1,op,e))
        return str(eval('*'.join(tmp)))
    elif op[idx] == '+':
        exps = exp.split('+')
        tmp = []
        for e in exps:
            tmp.append(calculate(idx+1,op,e))
        return str(eval('+'.join(tmp)))
    elif op[idx] == '-':
        exps = exp.split('-')
        tmp = []
        for e in exps:
            tmp.append(calculate(idx+1,op,e))
        return str(eval('-'.join(tmp)))

def solution(expression):
    answer = 0
    perm = permutations(['*','+','-'],3)
    for op in perm:
        answer = max(answer,abs(int(calculate(0,op,expression))))
    return answer
print(solution("100-200*300-500+20"))