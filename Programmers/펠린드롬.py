answer = False
def isPelindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]: return False
    return True
def checkAll(words,a,b,v,n,c):
    if c == n:
        global answer
        answer = True
    v[a] = True
    v[b] = True
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if v[i]==False and v[j]==False and (isPelindrome(words[i]+words[j])==True or isPelindrome(words[j]+words[i])==True):
                checkAll(words,i,j,v,n,c+2)
                v[i] = False
                v[j] = False
    
def solution(P):
    ans = []
    n = len(P)
    v = [False]*n
    global answer
    for j in range(1,n):
        answer = False
        if (isPelindrome(P[0]+P[j])==True or isPelindrome(P[j]+P[0])==True):
            checkAll(P,0,j,v,n,2)
            v[0] = False
            v[j] = False
        if answer == True:
            ans.append(P[j])
    return ans
print(solution(["21","123","111","11"]))