class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            div = set()
            for i in range(1, int(floor(sqrt(n))+1)):
                if n%i == 0:
                    div.add(n//i)
                    div.add(i)
                if len(div) > 4: break
            if len(div) == 4:
                res += sum(div)
        return res