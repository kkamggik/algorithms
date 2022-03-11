s = input()
alp = [0]*26
for i in s:
    alp[ord(i)-ord('a')] += 1
for i in alp: print(i,end=' ')