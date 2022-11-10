def binary(distance, rocks, n):
    # rocks = [2, 11, 14, 17, 21]
    rst = 0
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        remove_cnt = 0
        current = 0
        min_distance = 2e9
        for rock in rocks:
            diff = rock - current 
            if diff < mid:
                remove_cnt += 1
            else:
                current = rock
                min_distance = min(min_distance, diff) 
        if remove_cnt > n:
            right = mid - 1
        else:
            rst = min_distance
            left = mid + 1 
    return rst
def solution(distance, rocks, n):
    rocks.sort()
    answer = binary(distance, rocks, n)
    return answer