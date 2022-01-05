def exist(x):
    start,end = 0,n-1
    while start <= end:
        mid = (start+end)//2
        if cards[mid]==x: return 1
        elif x > cards[mid]:
            start = mid+1
        else:
            end = mid-1
    return 0
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
cards.sort()
for num in nums:
    print(exist(num),end=' ')
