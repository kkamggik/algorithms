from itertools import permutations 
def solution(k, dungeons):
    answer = -1
    permutation = permutations(dungeons, len(dungeons))
    for perm in permutation:
        cnt = 0
        tiredness = k
        for p in perm:
            if p[0] <= tiredness:
                tiredness -= p[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer
print(solution(	80, [[80, 20], [50, 40], [30, 10]]))