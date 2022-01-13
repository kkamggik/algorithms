a,b = map(str, input().split())
ans = str(int(a[::-1])+int(b[::-1]))
print(int(ans[::-1]))