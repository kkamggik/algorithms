s = input()
alp = [0]*26
for i in s.lower():
    alp[ord(i)-ord('a')] += 1
mx = max(alp)
if alp.count(mx) > 1: print('?')
else:
    idx = alp.index(mx)
    print(chr(ord('A')+idx))