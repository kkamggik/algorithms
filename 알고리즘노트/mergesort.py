def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    return arr