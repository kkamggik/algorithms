class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0]*num_people
        cnt = 1
        idx = 0
        while candies > 0:
            res[idx] += cnt if candies >= cnt else candies
            candies -= cnt
            cnt += 1
            idx += 1
            if idx == num_people: idx = 0
        return res