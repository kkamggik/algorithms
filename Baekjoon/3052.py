lst = [0]*42
for _ in range(10):
    t = int(input())
    lst[t%42] = 1
print(lst.count(1))