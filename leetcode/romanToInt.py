class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        # s = s.replace("IV","A")
        # s = s.replace("IX","B")
        # s = s.replace("XL","E")
        # s = s.replace("XC","F")
        # s = s.replace("CD","G")
        # s = s.replace("CM","H")
        # nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "A":4, "B":9, "E":40, "F":90, "G":400, "H":900}
        # for c in s:
        #     answer += nums[c]
        nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)-1):
            if nums[s[i]] < nums[s[i+1]]:
                answer -= nums[s[i]]
            else:
                answer += nums[s[i]]
        return answer+nums[s[-1]]
                