import sys
Y, X, M = map(int,input().split())
sharks = []
dy = [-1,1,0,0]
dx = [0,0,1,-1]
for _ in range(M): # y, x, 속도, 방향, 크기. 1234 -> 상하우좌
    temp = list(map(int,sys.stdin.readline().split()))
    temp[0] -= 1
    temp[1] -= 1
    temp[3] -= 1
    if(temp[3]== 0 or temp[3] == 1):
        temp[2] = temp[2] % ((Y-1) * 2)
    else:
        temp[2]= temp[2] % ((X-1) * 2)
    sharks.append(temp)

main_map = [[-1 for i in range(X)]for j in range(Y)]

#map 생성
for idx,shark in enumerate(sharks):
    main_map[shark[0]][shark[1]] = idx

ans = 0

def catch(fisher_x):
    target = -1
    ret = 0
    for y in range(Y):
        if(main_map[y][fisher_x] != -1):
            target = main_map[y][fisher_x]
            main_map[y][fisher_x] = -1
            break
    if(target != -1):
        ret = sharks[target][4]
        sharks[target][4] = -1
    return ret

def sharks_move():
    next_map = [[-1 for i in range(X)]for j in range(Y)]
    for idx,shark in enumerate(sharks):
        y, x, speed, dir, size = shark
        if(size == -1): #이미 잡히거나 죽은 상어
            continue
        for i in range(speed):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if(0<= ny < Y and 0<= nx < X):
                y = ny
                x = nx
            else:
                if(dir == 0): dir = 1
                elif(dir == 1): dir = 0
                elif(dir == 2): dir = 3
                elif(dir == 3): dir = 2
                y = y + dy[dir]
                x = x + dx[dir]
        #이동 완료
        sharks[idx][0] = y
        sharks[idx][1] = x
        sharks[idx][3] = dir
        sharks[idx][4] = size
        if(next_map[y][x] != -1): #이미 어떤 상어가 있는 경우
            target_shark = sharks[next_map[y][x]]
            if(target_shark[4] > size):
                sharks[idx][4] = -1
            else:
                sharks[next_map[y][x]][4] = -1
                next_map[y][x] = idx
        else:
            next_map[y][x] = idx
    return next_map
    #for idx,shark in enumerate(sharks):
    #    y, x, speed, dir, size = shark
    #    if(size == -1): #이미 잡히거나 죽은 상어
    #        continue
        

ans = 0
for fisher_x in range(X):
    ans += catch(fisher_x)
    main_map = sharks_move()

print(ans)