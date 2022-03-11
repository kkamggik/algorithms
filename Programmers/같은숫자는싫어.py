def solution(arr):
    prev = arr[0]
    answer = [prev]
    for i in arr[1:]:
        if prev == i: continue
        else:
            answer.append(i)
            prev = i
    return answer
print(solution([1,1,3,3,0,1,1]))