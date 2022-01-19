a,b,c = map(int, input().split())
if b >= c: print(-1)
else:
    equal = a//(c-b)
    print(equal+1)