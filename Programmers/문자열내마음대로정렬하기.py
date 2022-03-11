def solution(strings, n):
    answer = []
    for s in strings:
        s = list(s)
        answer.append(s)
    answer.sort()
    answer.sort(key = lambda x:x[n])
    rst = []
    for ans in answer:
        rst.append("".join(ans))
    return rst
print(solution(["sun", "bed", "car"],1))