while True:
    try:
        st = input()
        l,u,n,s = 0,0,0,0
        for i in st:
            if 'a'<=i<='z': l+=1
            elif 'A'<=i<='Z': u+=1
            elif i==' ': s+=1
            else: n+=1
        print(l,u,n,s)
    except EOFError:
        break
