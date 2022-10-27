def solution(ingredient):
    answer = 0
    stack = []
    order = [1,2,3,1]
    for ing in ingredient:
        stack.append(ing)
        if(len(stack) >= 4 and stack[-4:]==order):
            for i in range(4): stack.pop()
            answer += 1
    return answer