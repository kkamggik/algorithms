class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        a,b = "a","b"
        res = na = nb = 0
        if x < y:
            x,y = y,x
            a,b = b,a
        for c in s:
            if c==a: na += 1
            elif c==b:
                if na:
                    res += x
                    na -= 1
                else: nb += 1
            else:
                res += y*min(na,nb)
                na = nb = 0
        return res+y*min(na,nb)