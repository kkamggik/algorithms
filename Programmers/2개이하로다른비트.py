def solution(numbers):
    answer = []
    for number in numbers:
        if number%2==0:
            answer.append(number+1)
        else:
            n = '0'+bin(number)[2:]
            idx = n.rfind('0')
            n = list(n)
            n[idx] = '1'
            n[idx+1] = '0'
            n = ''.join(n)
            answer.append(int(n,2))
    return answer
print(solution([1,9,7]))