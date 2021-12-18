s = input()
ans = 0
prev = s[0]
for i in s[1:]:
    if prev != i:
        ans += 1
        prev = i
if ans%2==0:
    print(ans//2)
else:
    print(1+(ans//2))

# 다른 풀이법
# 1) 전부 1 로 바꾸기
# 2) 전부 0 으로 바꾸기
# count0 = 0
# count1 = 0
# if s[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         if s[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1
# print(min(count0, count1))