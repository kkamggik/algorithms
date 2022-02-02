t = 1
while True:
    arr = list(map(int, input().split()))
    if arr == [0,0,0]: break
    l,p,v = arr
    answer = (v//p)*l
    answer += min(l, (v%p))
    print("Case {}: {}".format(t, answer))
    t += 1