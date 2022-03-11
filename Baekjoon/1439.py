string = input()
flip = 0
prev = string[0]
for s in string[1:]:
    if prev!=s:
        prev = s
        flip += 1
if flip%2==0:
    flip//=2
else:
    flip//=2
    flip += 1
print(flip)