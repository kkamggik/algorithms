n = int(input())
coins = [500,100,50,10,5,1]
m = 1000-n
answer = 0
for i in coins:
    answer += m//i
    m %= i
print(answer)