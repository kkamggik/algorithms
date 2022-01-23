def solution(s):
    answer = []
    cnt,zeros = 0,0
    while True:
        if s == '1': return [cnt,zeros]
        zero = s.count('0')
        zeros += zero
        cnt += 1
        m = len(s)-zero
        s = bin(m)[2:]
print(solution("110010101001"))