class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        dist = []
        coords = [p1, p2, p3, p4]
        n = 4
        for i in range(n-1):
            for j in range(i+1,n):
                if coords[i] == coords[j]: return False
                d = (coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2
                dist.append(d**0.5)
        res = Counter(dist).most_common()
        return res[0][1] == 4 and res[1][1] == 2
