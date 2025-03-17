M,N = input().split()
M = int(M) # 가로
N = int(N) # 세로

box = []
for _ in range(N):
    box.append(list(map(int,input().split())))

ans = -1    
queue = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# queue initialize
for i in range(N):
    for j in range(M):
        if(box[i][j]==1):
            queue.append([i,j])

while(queue):
    ans += 1
    next_queue = []
    for tomato in queue:
        cur_y = tomato[0]
        cur_x = tomato[1]
        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            if(0<= next_y < N and 0<= next_x < M): #index 확인
                if(box[next_y][next_x] == 0): #안익은 토마토
                    next_queue.append([next_y,next_x])
                    box[next_y][next_x] = 1 #익기
    queue = next_queue

flag = 0
for i in range(N):
    for j in range(M):
        if(box[i][j] == 0):
            flag = 1

if(flag == 1):
    print(-1)
else:
    print(ans)