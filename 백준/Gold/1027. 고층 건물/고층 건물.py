N = int(input())
buildings = list(map(int,input().split()))
watchabale = [[0 for i in range(N)] for j in range(N)]
def pickTwoBuilding():
    ret = []
    for i in range(len(buildings)-1):
        for j in range(i+1,len(buildings)):
            temp = []
            temp.append(i)
            temp.append(j)
            ret.append(set(temp))
    return ret
        
def func(building):
    a = building[0]
    b = building[1]
    h_a = buildings[a]
    h_b = buildings[b]
    t = (h_a - h_b) / (a-b)
    for i in range(a+1,b):
        line_pos = t*i + h_a - t*a
        if(line_pos <= buildings[i]):
            return False
    return True


twoBuildings = pickTwoBuilding()
for two in twoBuildings:
    temp = list(two)
    temp.sort()
    a = temp[0]
    b = temp[1]
    if(func(temp)):
        watchabale[a][b] = 1
        watchabale[b][a] = 1

ans = []
for i in range(N):
    ans.append(sum(watchabale[i]))

print(max(ans))