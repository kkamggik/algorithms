from itertools import permutations
def check(user, banned):
    if len(user)!=len(banned): return False
    for i in range(len(user)):
        if banned[i]=='*': continue
        if banned[i]!=user[i]: return False
    return True
def solution(user_id, banned_id):
    answer = []
    permutation = permutations(user_id, len(banned_id))
    for perm in permutation:
        cnt = 0
        for user,banned in zip(perm, banned_id):
            if check(user,banned) == True: cnt += 1
        if cnt == len(banned_id):
            if set(perm) not in answer:
                answer.append(set(perm))
    return len(answer)
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))