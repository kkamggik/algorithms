class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res = [0]*(k+1)
        dic = {}
        for user, time in logs:
            if user not in dic:
                dic[user] = set()
            dic[user].add(time)
        for k, v in dic.items():
            res[len(v)] += 1
        return res[1:]