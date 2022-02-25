class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = min(strs,key=len)
        for i,char in enumerate(shortest):
            for string in strs:
                if string[i] != char: return shortest[:i]
        return shortest