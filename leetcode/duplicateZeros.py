class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        queue = deque()
        for a in arr:
            queue.append(a)
            if a==0: queue.append(a)
        for i in range(len(arr)):
            arr[i] = queue.popleft()
            
        