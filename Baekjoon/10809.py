s = input()
alp = [-1]*26
for i in range(len(s)):
    loc = ord(s[i])-ord('a')
    if alp[loc] == -1: alp[loc] = i
for i in alp: print(i,end=' ')
