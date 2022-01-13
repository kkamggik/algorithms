def solution(arr, divisor):
    answer = []
    for a in arr:
        if a%divisor == 0:
            answer.append(a)
    answer.sort()
    if not answer: return [-1]
    return answer
print(solution([2, 36, 1, 3],1))