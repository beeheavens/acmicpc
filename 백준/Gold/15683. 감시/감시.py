from itertools import product
N, M = map(int,input().split())
main_map = []
for _ in range(N):
    main_map.append(list(map(int,input().split())))

cctv = []

def watch(source,dir,mapp):
    c_y = source[0]
    c_x = source[1]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    n_y = c_y + dy[dir]
    n_x = c_x + dx[dir]
    while(0<=n_y < N and 0<=n_x < M):
        if(mapp[n_y][n_x] == 0):
            mapp[n_y][n_x] = '#'
        elif(mapp[n_y][n_x] == 6):
            break
        n_y = n_y + dy[dir]
        n_x = n_x + dx[dir]

    return mapp

def count(mapp):
    ret = 0
    for i in range(N):
        for j in range(M):
            if(mapp[i][j] == 0):
                ret += 1
    return ret

for i in range(N):
    for j in range(M):
        if(1<=main_map[i][j]<=5):
            cctv.append([main_map[i][j],[i,j]])

directions = list(product([0,1,2,3],repeat = len(cctv))) #가능한 방향들 전부 잡음

ans = float("inf")
for d in directions:
    temp_map = [row[:] for row in main_map]
    for i in range(len(cctv)):
        cctv_pos = cctv[i][1]
        cctv_shape = cctv[i][0]
        if(cctv_shape == 1):
            temp_map = watch(cctv_pos,d[i],temp_map)
        elif(cctv_shape == 2):
            if(d[i] == 0 or d[i] == 2):
                temp_map = watch(cctv_pos,0,temp_map)
                temp_map = watch(cctv_pos,2,temp_map)
            else:
                temp_map = watch(cctv_pos,1,temp_map)
                temp_map = watch(cctv_pos,3,temp_map)
        elif(cctv_shape == 3):
            temp_map = watch(cctv_pos,d[i],temp_map)
            temp_map = watch(cctv_pos,(d[i]+1)%4,temp_map)
        elif(cctv_shape == 4):
            temp_map = watch(cctv_pos,d[i],temp_map)
            temp_map = watch(cctv_pos,(d[i]+1)%4,temp_map)
            temp_map = watch(cctv_pos,(d[i]+2)%4,temp_map)
        elif(cctv_shape == 5):
            for k in range(4):
                temp_map = watch(cctv_pos,k,temp_map)
    sagak = count(temp_map)
    if(ans > sagak):
        ans = sagak

print(ans)