class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        arr = [0]*(n+2)
        for book in bookings:
            a,b,c = book
            arr[a] += c
            arr[b+1] -= c
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        return arr[1:-1]