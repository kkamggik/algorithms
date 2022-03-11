def solution(a, b, g, s, w, t):
    answer = -1
    left,right = 0, int(1e9 * 2 * 1e5 * 2)
    n = len(g)
    while left <= right:
        mid = (left+right)//2
        total_silver = 0
        total_gold = 0
        total = 0
        for i in range(n):
            r = t[i]*2
            time = mid//r
            if mid%r >= t[i]: time += 1
            total_silver += min(s[i], time*w[i])
            total_gold += min(g[i], time*w[i])
            total += min(g[i]+s[i], time*w[i])
        if total_gold >= a and total_silver >= b and total >= a+b:
            right = mid - 1
        else:
            left = mid + 1
    return left