def solution(word):
    answer = 0
    dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    num = [781, 156, 31, 6, 1]
    idx = 0
    for w in word:
        answer += (num[idx]*dic[w])+1
        idx += 1
    return answer
print(solution("EIO"))