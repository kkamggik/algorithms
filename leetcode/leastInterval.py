class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks).values()
        M = max(counter)
        Mct = counter.count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)