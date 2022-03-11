def solve(str1,str2):
    s1,s2,dic = {},{},{}
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s = str1[i]+str1[i+1]
            if s in s1: s1[s] += 1
            else: s1[s] = 1
            if s in dic: dic[s] += 1
            else: dic[s] = 1
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s = str2[i]+str2[i+1]
            if s in s2: s2[s] += 1
            else: s2[s] = 1
            if s in dic: dic[s] = max(dic[s],s2[s])
            else: dic[s] = 1
    mn,mx = 0,0
    for k,v in dic.items():
        mx += dic[k]
    for k,v in s1.items():
        if k in s2 and s2[k] > 0:
            cnt = min(v, s2[k])
            mn += cnt
    if mn==0 and mx==0: return 1
    return mn/mx
def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    rst = solve(str1,str2)
    return int(rst*65536)
print(solution("E=M*C^2", "e=m*c^2"))