N, K = map(int,input().split())
global tank
tank = [list(map(int,input().split()))]

def check(): # 물고기 수 차이 체크
    if((max(tank[0]) - min(tank[0])) <= K):
        return False
    return True

def add_fish(): #물고기 수를 추가
    target = min(tank[0])
    for idx,value in enumerate(tank[0]):
        if value == target:
            tank[0][idx] += 1

def roll_tank():
    global tank
    tank.insert(0,[tank[0][0]])
    del tank[1][0]
    while(len(tank) <= (len(tank[len(tank)-1]) - len(tank[0]))):
        new_tank = []
        for i in range(len(tank[0])):
            temp = []
            for j in range(len(tank)-1,-1,-1):
                temp.append(tank[j][i])
            new_tank.append(temp)
        temp = []
        for i in range(len(tank[0]),len(tank[len(tank)-1])):
            temp.append(tank[len(tank)-1][i])
        new_tank.append(temp)
        tank = new_tank

def control_fish():
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    diff_table = []
    for i in tank: # 원본 어항과 같은 모양의 Diff_table 만들기
        temp = []
        for j in i:
            temp.append(0)
        diff_table.append(temp)
    
    for idx_y,row in enumerate(tank):
        for idx_x,value in enumerate(row):
            for d in range(4):
                next_y = idx_y + dy[d]
                next_x = idx_x + dx[d]
                if(0<= next_y < len(tank) and 0<= next_x < len(row)): # 인덱스 체크를 해주고
                    try: #try를 써줘야 함. 어항들이 직사각형으로 배치된 게 아니기 때문
                        if(value > tank[next_y][next_x]):
                            diff = (value - tank[next_y][next_x]) // 5
                            diff_table[idx_y][idx_x] -= diff
                            diff_table[next_y][next_x] += diff
                    except:
                        pass
    for idx_y,row in enumerate(tank):
        for idx_x,value in enumerate(row):
            tank[idx_y][idx_x] += diff_table[idx_y][idx_x]
    
def serialize():
    global tank
    new_tank = []
    temp = []
    for i in range(len(tank[0])):
        for j in range(len(tank)-1,-1,-1):
            temp.append(tank[j][i])
    for i in range(len(tank[0]),len(tank[len(tank)-1])):
        temp.append(tank[len(tank)-1][i])
    new_tank.append(temp)
    tank = new_tank 

def second_roll():
    global tank
    #first
    new_tank = []
    temp = []
    for i in range(len(tank[0])//2-1,-1,-1):
        temp.append(tank[0][i])
    new_tank.append(temp)
    temp = []
    for i in range(len(tank[0])//2,len(tank[0])):
        temp.append(tank[0][i])
    new_tank.append(temp)
    tank = new_tank
    #second
    target = []
    temp =[]
    for i in range(len(tank[0])//2):
        temp.append(tank[0][i])
    target.append(temp)
    temp = []
    for i in range(len(tank[0])//2):
        temp.append(tank[1][i])
    target.append(temp)
    new_tank = []
    for i in range(1,-1,-1):
        temp = []
        for j in range(len(target[0])-1,-1,-1):
            temp.append(target[i][j])
        new_tank.append(temp)
    for i in range(len(tank)):
        temp = []
        for j in range(len(tank[0])//2,len(tank[0])):
            temp.append(tank[i][j])
        new_tank.append(temp)
    tank = new_tank

def second_serialize():
    global tank
    new_tank = []
    for j in range(len(tank[0])):
        for i in range(len(tank)-1,-1,-1):
            new_tank.append(tank[i][j])
    tank = [new_tank]


ans = 0
while(check()):
    ans += 1
    add_fish()
    roll_tank()
    control_fish()
    serialize()
    second_roll()
    control_fish()
    second_serialize()
print(ans)