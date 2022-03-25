class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        i, n = 0, len(barcodes)
        res = [0] * n
        counter = Counter(barcodes).most_common()
        for k, v in counter:
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n: i = 1
        return res