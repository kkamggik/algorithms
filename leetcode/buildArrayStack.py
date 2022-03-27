class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []
        val = 1
        idx = 0
        while idx < len(target):
            if val <= target[idx]:
                stack.append(val)
                val += 1
                res.append("Push")
            else: idx += 1
            if stack and stack[-1] not in target:
                stack.pop()
                res.append("Pop")
            if stack and stack[-1] == n: break
        return res