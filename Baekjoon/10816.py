def first(x):
    start,end = 0,len(cards)-1
    while start <= end:
        mid = (start+end)//2
        if (mid==0 or x > cards[mid-1]) and cards[mid]==x:
            return mid
        elif cards[mid] >= x:
            end = mid-1
        else:
            start = mid+1
    return -1
def last(x):
    start,end = 0,len(cards)-1
    while start <= end:
        mid = (start+end)//2
        if (mid==len(cards)-1 or x < cards[mid+1]) and cards[mid]==x:
            return mid
        elif cards[mid] > x:
            end = mid-1
        else:
            start = mid+1
    return -1
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
cards.sort()
for num in nums:
    s,e = first(num),last(num)
    if s==-1 and e==-1: ans = 0
    else: ans = e-s+1
    print(ans,end=' ')
