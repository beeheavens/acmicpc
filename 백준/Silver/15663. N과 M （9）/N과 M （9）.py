from itertools import permutations
n,m = map(int,input().split())

num = list(map(int,input().split()))

combi = list(permutations(num,m))

dict = {}
for i in combi:
    if(i not in dict):
        dict[i] = 1
    else:
        pass

temp = []
for i in dict:
    temp.append(list(i))

temp.sort()
for i in temp:
    for j in i:
        print(j,end=" ")
    print()