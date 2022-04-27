class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {'1':0, '10':0, '010':0, '0':0, '01':0, '101':0}
        for c in s:
            if c=='0':
                res[c] +=  1
                res['10'] += res['1']
                res['010'] += res['01']
            else:
                res[c] +=  1
                res['01'] += res['0']
                res['101'] += res['10']
        return res['101']+res['010']
            