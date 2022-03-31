class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k==0: return [0]*len(code)
        res = [0]*len(code)
        for i in range(len(code)):
            val = 0
            for j in range(1,abs(k)+1):
                if k > 0: val += code[(i+j)%(len(code))]
                else: val += code[(i-j)%len(code)]
            res[i] = val
        return res
        
        