class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        n = len(tops)
        top = defaultdict(int)
        btm = defaultdict(int)
        same = 0
        for t,b in zip(tops, bottoms):
            top[t] += 1
            btm[b] += 1
            if t == b: same += 1
        answer = 1e9
        for i in range(1,7):
            if(top[i]+btm[i]-same == n):
                return n - max(top[i],btm[i])
        return -1
