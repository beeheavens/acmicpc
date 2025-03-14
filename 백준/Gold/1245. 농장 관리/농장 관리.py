## DFS
def dfs(farm,start): # dfs -> visited, stack
    visited = []
    stack = [start]
    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,1,1,1,0,-1,-1,-1]
    while(stack):
        cur = stack.pop() # stack에서 꺼내기
        visited.append(cur)
        cur_x = cur[1]
        cur_y = cur[0]
        for d in range(8):
            next_y = cur_y + dy[d]
            next_x = cur_x + dx[d]
            if(0 <= next_y < N and 0 <= next_x < M): #index 체크
                if(farm[cur_y][cur_x]<farm[next_y][next_x]): # 인접에 더 높은 곳이 있는 경우
                    return 0
                elif(farm[cur_y][cur_x] == farm[next_y][next_x]): #인접에 같은 높이가 있는 경우    
                    if([next_y,next_x] not in stack and [next_y,next_x] not in visited):
                        stack.append([next_y,next_x])
    for i in visited:
        top.append(i)
    return 1

N,M = input().split() # 가로 세로
N = int(N)
M = int(M)

# 농장 맵 생성
farm = []
top = []
for _ in range(N):
    farm.append(list(map(int,input().split())))

ans = 0
for y in range(N):
    for x in range(M):
        if(farm[y][x] != 0 and [y,x] not in top): # 산의 일부인 경우 dfs로 산봉우리를 구해냄
            if(dfs(farm,[y,x])==1):
                ans += 1

print(ans)
