answer = 0
prime = [True]*(3001)
prime[1] = False
for i in range(2,3001):
    for j in range(i+i,3001,i):
        prime[j] = False
def three(arr,idx,cnt,s):
    if cnt == 3:
        global answer
        if prime[s] == True: answer+=1
        return
    for j in range(idx+1,len(arr)):
        three(arr,j,cnt+1,s+arr[j])
def solution(nums):
    for i in range(len(nums)-2):
        three(nums,i,1,nums[i])
    return answer
print(solution([1,2,7,6,4]))