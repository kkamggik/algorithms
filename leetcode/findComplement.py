class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = bin(num)
        res = ''
        for c in s[2:]:
            if c=='1': res += '0'
            else: res += '1'
        return int(res, 2)
        