def binary(n, times):
    left, right = 0, pow(1000000000,2)
    answer = right
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
        if(cnt >= n):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
def solution(n, times):
    answer = binary(n, times)
    return answer