from itertools import combinations
def solution(relation):
    answer = 0
    keys = [i for i in range(len(relation[0]))]
    columns = [0]*len(relation[0])
    candidates = []
    for i in range(1,len(keys)+1):
        comb = combinations(keys,i)
        for c in comb:
            exist = False
            for candidate in candidates:
                if set(candidate).issubset(set(c)): 
                    exist = True
                    break
            if not exist:
                temp = set()
                for j in range(len(relation)):
                    t = ''
                    for d in c: t += relation[j][d] + ' '
                    temp.add(t)
                if len(temp) == len(relation): 
                    candidates.append(c)
                    answer += 1
    return answer
print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))