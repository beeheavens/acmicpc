str = input()
alphabets = [-1 for i in range(26)]
cur = 0
for i in str:
    if(alphabets[ord(i)-ord('a')]== -1):
        alphabets[ord(i)-ord('a')] = cur
    cur += 1

for i in alphabets:
    print(i,end=' ')