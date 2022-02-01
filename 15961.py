from collections import defaultdict
n,d,k,c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.extend(arr)
left, right = 0,0
dic = defaultdict(int)
answer = 0
dic[c] += 1
while right < k:
    dic[arr[right]] += 1
    right += 1
while right < len(arr):
    answer = max(answer, len(dic))
    dic[arr[left]] -= 1
    if dic[arr[left]] == 0:
        del dic[arr[left]]
    left += 1
    dic[arr[right]] += 1
    right += 1
print(answer)
