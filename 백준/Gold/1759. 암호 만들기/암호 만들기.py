from itertools import combinations

l, c = map(int,input().split())
alphabet = list(map(str,input().split()))
alphabet.sort()

combi = list(combinations(alphabet,l))
for i in combi:
    i = list(i)
    vowel = 0
    for char in i:
        if(char in ['a','e','i','o','u']):
            vowel += 1
    if(vowel >= 1 and len(i) - vowel >= 2):
        for j in i:
            print(j,end="")
        print()