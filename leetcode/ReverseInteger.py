class Solution(object):
    def reverse(self, x):
        sign = 1
        if x<0: sign = -1
        answer = sign*(int(str(abs(x))[::-1]))
        if -2**31 <= answer <= (2**31)-1: return answer
        return 0
        