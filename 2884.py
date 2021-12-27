h,m = map(int, input().split())
nm = (m-45)%60
if nm > m: h -= 1
nh = h % 24
print(nh,nm)