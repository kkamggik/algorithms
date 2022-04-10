class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = []
        for c in ops:
            if c=='C': score.pop()
            elif c=='D': score.append(score[-1]*2)
            elif c=='+': score.append(score[-1]+score[-2])
            else: score.append(int(c))
        return sum(score)