def solution(price, money, count):
    rst = 0
    for i in range(1,count+1):
        rst += price*i
    if money >= rst: return 0
    return rst - money