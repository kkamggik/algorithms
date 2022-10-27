def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        if(word in words): answer += 1
        else:
            idx = 0
            prev = -1
            while (idx < len(word)):
                flag = False
                for i in range(4):
                    if(word[idx:idx+len(words[i])]==words[i] and prev!=i):
                        idx += len(words[i])
                        flag = True
                        prev = i
                        break
                if(flag == False): break
            if(idx == len(word)): answer += 1
    return answer

