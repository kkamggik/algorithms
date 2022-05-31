class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        res = []
        for rest in restaurants:
            if veganFriendly==1 and rest[2]==0: continue
            if rest[3]<=maxPrice and rest[4]<=maxDistance:
                res.append(rest)
        res.sort(key = lambda x:(-x[1],-x[0]))
        ans = [r[0] for r in res]
        return ans
