parent = input().strip()
pattern = input().strip()
# KMP Algorithm
# 시간복잡도는 O(N+M)
check = 0
# make table
table = [0]*(len(pattern)+1)
j = 0
for i in range(1, len(pattern)):
    while(j>0 and pattern[i]!=pattern[j]):
        j = table[j-1]
    if(pattern[i]==pattern[j]):
        j += 1
        table[i] = j
# KMP algorithm
j = 0
for i in range(0, len(parent)):
    while(j>0 and parent[i]!=pattern[j]):
        j = table[j-1]
    if(parent[i] == pattern[j]):
        if(j == len(pattern)-1):
            check = 1
            j = table[j]
        else:
            j += 1
print(check)