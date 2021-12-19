s = input()
rst = []
num = 0
for c in s:
    if ord('A')<=ord(c)<=ord('Z'):
        rst.append(c)
    else:
        num += int(c)
rst.sort()
print(''.join(rst)+str(num))
