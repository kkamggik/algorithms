class Solution(object):
    def myAtoi(self, s):
        digit = ''
        number = s.split()
        if not number: return "0"
        number = number[0]
        sign = 0
        allow = True
        for c in number:
            if not c.isdigit():
                if not allow: break
                elif c=='-' and sign==0:
                    sign = -1
                    allow = False
                elif c=='+' and sign==0:
                    sign = 1
                    allow = False
                elif c==' ' and allow: continue
                else: break
            else:
                digit += c
                allow = False
        if not digit: return "0"
        if sign==0: sign = 1
        number = sign*int(digit)
        if number <= -2**31: return -2**31
        elif number >= (2**31)-1: return (2**31)-1
        return number