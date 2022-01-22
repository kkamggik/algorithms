def check(skill, user_skill):
    idx = 0
    for s in user_skill:
        if s not in skill: continue
        if s != skill[idx]: return False
        else:
            idx += 1
    return True
def solution(skill, skill_trees):
    answer = 0
    for user_skill in skill_trees:
        if check(skill, user_skill) == True: answer += 1
    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))