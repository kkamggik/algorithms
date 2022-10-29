def check(number, answer):
    for i in range(len(number)):
        if(answer[i] < number[i]): return 0
    return 1
def solution(want, number, discount):
    answer = [0]*len(want)
    rst = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = i
    for i in range(len(discount)):
        if(discount[i] in dic): answer[dic[discount[i]]] += 1
        if(i >= 10 and discount[i-10] in dic): answer[dic[discount[i-10]]] -= 1
        rst += check(number, answer)
    return rst
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))