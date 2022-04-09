class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        idx1 = idx2 = 0
        res = []
        while idx1 < len(firstList) and idx2 < len(secondList):
            s1,e1 = firstList[idx1]
            s2,e2 = secondList[idx2]
            if s1 <= e2 and s2 <= e1:
                res.append([max(s1,s2), min(e1,e2)])
            if e1 <= e2: idx1 += 1
            else: idx2 += 1 
        return res