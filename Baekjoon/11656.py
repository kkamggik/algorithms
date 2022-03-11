s = input()
ans = [s]
for i in range(1,len(s)):
    ans.append(s[i:])
ans.sort()
for a in ans: print(a)