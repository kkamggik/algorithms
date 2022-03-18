class Solution(object):
    def combination(self, idx, cnt, lst, curr, k):
        if len(curr) == k:
            global answer
            answer.append(curr[:])
        for i in range(idx, len(lst)):
            curr.append(lst[i])
            self.combination(i+1, cnt+1, lst, curr, k)
            curr.pop()
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        lst = [i for i in range(1,n+1)]
        m = n - k + 1
        global answer
        answer = []
        self.combination(0,0,lst,[],k)
        return answer
