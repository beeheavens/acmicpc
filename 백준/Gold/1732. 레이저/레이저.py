import sys
N = int(sys.stdin.readline())
buildings = []
for _ in range(N):
    buildings.append(list(map(int,sys.stdin.readline().split())))

buildings.sort(key = lambda x : (x[0]**2 + x[1]**2))

dict = {}
ans = []

for i in buildings:
    if i[1] == 0 and  i[0] > 0:
        g = "plusinf"
    elif i[1] == 0 and i[0] < 0:
        g = "minusinf"
    elif i[0] == 0 and i[1] < 0:
        g = "minusinf2"
    elif i[0] == 0 and i[1] > 0:
        g = "plusinf2"
    else:
        g = i[0]/i[1]
    if g in dict:
        dict[g].append(i)
    else:
        dict[g] = [i]

for g in dict:
    targets = dict[g]
    for i in range(len(targets)):
        target = targets[i]
        for j in range(i):
            if(targets[j][2] >= target[2]):
                ans.append([target[0],target[1]])
                break

ans.sort()
for i in ans:
    print(i[0],i[1])