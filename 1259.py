while True:
    s = input()
    if s=='0': break
    ans = 'yes'
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]: 
            ans = 'no'
            break
    print(ans)