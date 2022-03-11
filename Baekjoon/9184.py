import sys
input = sys.stdin.readline
def recursive(a,b,c):
    global dic
    s = str(a)+' '+str(b)+' '+str(c)
    if s in dic: return dic[s]
    if a<=0 or b<=0 or c<=0: 
        dic[s] = 1
    elif a > 20 or b > 20 or c > 20:
        dic[s] = recursive(20,20,20)
    elif a < b and b < c:
        dic[s] = recursive(a,b,c-1) + recursive(a,b-1,c-1) - recursive(a,b-1,c)
    else:
        dic[s] = recursive(a-1,b,c) + recursive(a-1,b-1,c) + recursive(a-1,b,c-1) - recursive(a-1,b-1,c-1)  
    return dic[s]

dic = {}
while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1: break
    answer = recursive(a,b,c)
    print('w({}, {}, {}) = {}'.format(a,b,c,answer))