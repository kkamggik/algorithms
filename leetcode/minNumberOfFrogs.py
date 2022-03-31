class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        c = r = o = a = k = use = 0
        res = 0
        for char in croakOfFrogs:
            if char=='c':
                c += 1
                use += 1
            elif char=='r': r += 1
            elif char=='o': o += 1 
            elif char=='a': a += 1
            elif char=='k':
                k += 1
                use -= 1
            res = max(res, use)
            if c < r or r < o or o < a or a < k: return -1
        if use!=0 or not(c==r and r==o and o==a and a==k and k==c): return -1
        return res