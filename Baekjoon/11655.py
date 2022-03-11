s = input()
ans = ''
for i in s:
    if 'a'<=i<='z':
        t = (ord(i)-97+13)%26
        ans += chr(t+97)
    elif 'A'<=i<='Z':
        t = (ord(i)-65+13)%26
        ans += chr(t+65)
    else: ans += i
print(ans)