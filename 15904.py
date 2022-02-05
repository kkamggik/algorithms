s = input().strip()
answer = ''
for w in s:
    if w.isupper(): answer += w
word = ['U','C','P','C']
rst = False
idx = 0
for w in answer:
    if word[idx] == w:
        idx += 1
        if idx == 4:
            rst = True
            break
if rst == True: print('I love UCPC')
else: print('I hate UCPC')
