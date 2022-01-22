def convert(n,q):
    num = ''
    while n > 0:
        if n%q < 10:
            num += str(n%q)
        else:
            num += chr(n%q-10+65)
        n //= q
    if num=='': return '0'
    return num[::-1]