def solution(number, k):
    stack = [number[0]]
    curr = 0
    for i in number[1:]:
        n = int(i)
        while(stack and curr < k and int(stack[-1]) < n):
            stack.pop(-1)
            curr += 1
        stack.append(i)
    answer = ''.join(stack[:len(number)-k])
    return answer

print(solution("654321", 5))