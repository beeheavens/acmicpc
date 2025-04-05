from itertools import combinations
N,M = map(int,input().split())

nums = [i for i in range(1,N+1)]
combi = list(combinations(nums,M))
temp = []
for i in combi:
    temp.append(list(i))
temp.sort()
for i in temp:
    for j in i:
        print(j,end=" ")
    print()