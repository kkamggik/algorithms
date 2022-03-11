import sys
input = sys.stdin.readline
def combination(consonant, vowel, length, idx, word):
    if idx == m or length==n:
        if length==n and consonant >= 2 and vowel >= 1:
            print(''.join(word))
        return
    for i in range(idx, m):
        word[length] = arr[i]
        if arr[i] in ['a','e','i','o','u']:
            combination(consonant, vowel+1, length+1, i+1, word)
        else:
            combination(consonant+1, vowel, length+1, i+1, word)
        word[length] = ''
n,m = map(int, input().split())
arr = list(map(str, input().strip().split()))
arr.sort()
combination(0,0,0,0,['']*n)