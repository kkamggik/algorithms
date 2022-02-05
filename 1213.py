word = input().strip()
alp = [0]*26
for w in word:
    alp[ord(w)-ord('A')] += 1
cnt = 0
odd = ''
answer = ''
for i in range(26):
    if alp[i]%2==1: 
        cnt += 1
        odd += chr(i+65) 
    answer += chr(i+65)*(alp[i]//2)
if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer + odd + answer[::-1])

