class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        res = 0
        dic = defaultdict(int)
        for d in deliciousness:
            for i in range(22):
                res += dic[2**i - d]
            dic[d] += 1
        return res%(10**9 + 7)
                