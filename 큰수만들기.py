def solution(number, k):
    answer = ''
    stack = []
    rem = len(number)-k
    for n in range(len(number)):
        num = number[n]
        if n < k:
            while stack and stack[-1] < num:
                stack.pop()
        else:
            if num > stack[-1]:
                left = len(number)-n
                while len(stack)+left > rem and stack[-1]<num:
                    stack.pop()
        stack.append(num)
    return ''.join(stack[:rem])
print(solution(	"4177252846", 2))