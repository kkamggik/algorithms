t = int(input())
for _ in range(t):
    h,w,n = map(int, input().split())
    if n%h == 0:
        floor = h
        room = n//h
    else:
        floor = n%h
        room = (n//h)+1
    floor = str(floor)
    if room < 10: room = '0'+str(room)
    else: room = str(room)
    print(floor+room)