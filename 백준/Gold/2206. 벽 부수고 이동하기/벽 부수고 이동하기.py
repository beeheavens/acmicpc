from collections import deque
N, M = map(int,input().split())

main_map = []
for _ in range(N):
    temp = []
    string = input()
    for i in string:
        temp.append(int(i))
    main_map.append(temp)

dp = [[[0,0]for i in range(M)]for j in range(N)]

dp[0][0][0] = 1
bfs = deque()
bfs.append([0,0,0])
dy = [0,1,0,-1]
dx = [1,0,-1,0]
while(bfs):
    cur = bfs.popleft()
    cy,cx,cz = cur
    for d in range(4):
        ny = cy + dy[d]
        nx = cx + dx[d]
        cdp = dp[cy][cx][cz]
        if(0<= ny < N and 0<= nx < M):
            if(main_map[ny][nx]==0): # 벽 아님
                if(dp[ny][nx][cz] == 0 or dp[ny][nx][cz] > cdp+1):
                    dp[ny][nx][cz] = cdp + 1
                    bfs.append([ny,nx,cz])
            elif(main_map[ny][nx]==1): #벽인경우
                if(cz == 0):
                    if(dp[ny][nx][cz+1] == 0 or dp[ny][nx][cz+1] > cdp+1):
                        dp[ny][nx][cz+1] = cdp+1
                        bfs.append([ny,nx,cz+1])

if(sum(dp[N-1][M-1]) == 0):
    print(-1)
elif(0 in dp[N-1][M-1]):
    print(max(dp[N-1][M-1]))
else:
    print(min(dp[N-1][M-1]))