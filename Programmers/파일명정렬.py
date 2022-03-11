def convert(f):
    head,number,tail = 1,0,0
    name = []
    t = ''
    for s in range(len(f)):
        if number and not f[s].isdigit():
            name.append(int(t))
            name.append(f[s:])
            return name
        elif number and f[s].isdigit():
            t += f[s]
        elif head and not f[s].isdigit():
            t += f[s]
        elif head and f[s].isdigit():
            name.append(t.lower())
            number = 1
            t = f[s]
    name.append(int(t))
    name.append('')
    return name
def solution(files):
    answer = []
    arr = []
    for f in files:
        head,number,tail = convert(f)
        arr.append([head,number,tail,f])
    arr.sort(key = lambda x:(x[0],x[1]))
    print(arr)
    for a in arr: answer.append(a[3])
    return answer
print(solution(["img000012345", "img1.png","img2","IMG02"]))