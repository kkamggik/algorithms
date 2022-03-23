n,m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0,max(trees)
while left <= right:
    mid = (left+right)//2
    rem = 0
    for tree in trees:
        if tree-mid > 0: rem += (tree-mid)
    if rem >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)