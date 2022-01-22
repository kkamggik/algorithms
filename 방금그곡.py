def convert(a,b):
    h1,m1 = a.split(':')
    h2,m2 = b.split(':')
    h1,h2,m1,m2 = int(h1),int(h2),int(m1),int(m2)
    mins = 0
    if m2 < m1:
        h2 -= 1
        mins = m2+60-m1
    else: mins = m2-m1
    mins += (h2-h1)*60
    return mins
def full(music, time):
    r = 1
    if len(music) < time:
        r = (time//len(music))+1
    return music*r
def solution(m, musicinfos):
    answer = [-1,'']
    m = m.replace('C#','H')
    m = m.replace('D#','I')
    m = m.replace('F#','J')
    m = m.replace('G#','K')
    m = m.replace('A#','L')
    for musicinfo in musicinfos:
        t1,t2,title,code = musicinfo.split(',')
        time = convert(t1,t2)
        code = code.replace('C#','H')
        code = code.replace('D#','I')
        code = code.replace('F#','J')
        code = code.replace('G#','K')
        code = code.replace('A#','L')
        music = full(code, time)
        music = music[:time+1]
        if m in music:
            if time > answer[0]:
                answer = [time,title]
    if answer[0]==-1: return "(None)"
    return answer[1]
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))