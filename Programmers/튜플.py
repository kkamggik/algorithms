from collections import Counter
def solution(s):
    answer = []
    s = s.replace("{","")
    s = s.replace("}","")
    s = s.split(",")
    counter = Counter(s)
    ans = counter.most_common()
    print(ans)
    for a in ans:
        answer.append(int(a[0]))
    return answer
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))