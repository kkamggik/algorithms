class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        check = [0]*51
        for lst in ranges:
            for i in range(lst[0],lst[1]+1):
                check[i] = 1
        for i in range(left, right+1):
            if check[i]==0: return False
        return True