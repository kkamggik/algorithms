class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        answer = []
        for query in queries:
            idx = 0
            flag = True
            for c in query:
                if idx<len(pattern) and pattern[idx] == c:
                    idx += 1
                elif c.isupper():
                    flag = False
                    break
            if idx<len(pattern): flag = False
            answer.append(flag)
        return answer