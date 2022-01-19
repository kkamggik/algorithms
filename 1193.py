n = int(input())
line = 1
cnt = 1
while n > cnt:
     line += 1
     cnt += line
if line%2==1:
    left = cnt - n
    top = left + 1
    btm = line - left
else:
    left = cnt - n
    top = line - left
    btm = left + 1
print(str(top)+'/'+str(btm))