if ord('a')<=ord(i)<=ord('z'):
    i = (ord(i)-ord('a')+n)%26
    answer += chr(i+97)
else:
    i = (ord(i)-ord('A')+n)%26
    answer += chr(i+65)