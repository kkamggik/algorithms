s = input()
idx = 0
rst = 0
l = len(s)
while idx < l:
    if s[idx] in ['c','s','z']:
        if idx+1 < l and s[idx+1] == '=':
            idx += 1
    if s[idx] in ['c','d']:
        if idx+1 < l and s[idx+1] == '-':
            idx += 1
    if s[idx] in ['l','n']:
        if idx+1 < l and s[idx+1] == 'j':
            idx += 1
    if s[idx]=='d':
        if idx+2 < l and s[idx+1]=='z' and s[idx+2]=='=':
            idx += 2
    idx += 1
    rst += 1
print(rst)
    
