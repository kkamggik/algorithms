string = input()
curr = int(string[0])
for i in string[1:]:
    curr = max(curr+int(i), curr*int(i))
print(curr)