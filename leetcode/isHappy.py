class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = str(n)
        exist = set()
        while num!="1":
            if num in exist: return False
            exist.add(num)
            answer = 0
            for s in num:
                answer += int(s)**2
            num = str(answer)
        return True
        