class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        queue = deque([s])
        rst = set([s])
        while queue:
            s = queue.popleft()
            s1 = s[-b:]+s[:-b]
            if s1 not in rst:
                rst.add(s1)
                queue.append(s1)
            s2 = "".join([str((int(c)+a*(i%2))%10) for i,c in enumerate(s)])
            if s2 not in rst:
                rst.add(s2)
                queue.append(s2)            
        return min(rst)