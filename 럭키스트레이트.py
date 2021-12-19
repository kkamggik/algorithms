score = input()
left,right = 0,0
for i in range(len(score)//2):
    left += int(score[i])
    right += int(score[-i-1])
if left==right:
    print('LUCKY')
else:
    print('READY')