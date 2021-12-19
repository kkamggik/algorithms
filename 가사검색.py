from bisect import bisect_right, bisect_left
def count(a, left_val, right_val):
    right = bisect_right(a, right_val)
    left = bisect_left(a, left_val)
    return right - left
words = list(map(str, input().split()))
queries = list(map(str, input().split()))
arr = [[] for _ in range(10001)]
rev = [[] for _ in range(10001)]
answer = []
for word in words:
    arr[len(word)].append(word)
    rev[len(word)].append(word[::-1])
for i in range(10001):
    arr[i].sort()
    rev[i].sort()
for query in queries:
    if query[0] != '?':
        rst = count(arr[len(query)], query.replace('?','a'), query.replace('?','z'))
    else:
        rst = count(rev[len(query)], query[::-1].replace('?','a'), query[::-1].replace('?','z'))
    answer.append(rst)
print(answer)