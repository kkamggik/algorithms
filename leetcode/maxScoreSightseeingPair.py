class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = res = 0
        for i, v in enumerate(values):
            # here v - i is actually `A[j] - j` in the formula
            res = max(res, v - i + best)
            # here we store `A[i] + i`
            best = max(best, v + i)
        return res