from collections import deque
N = int(input())
grid = []
for _ in range(N):
    temp = input()
    temp_list = []
    for i in temp:
        temp_list.append(i)
    grid.append(temp_list)

def bfs(start):
    ret = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    target = grid[start[0]][start[1]]
    q.append(start)
    while(q):
        cur = q.popleft()
        ret.append(cur)
        cy = cur[0]
        cx = cur[1]
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if(0<= ny < len(grid) and 0<=nx<len(grid)):
                if(grid[ny][nx] == target and [ny,nx] not in ret and [ny,nx] not in q):
                    q.append([ny,nx])
    return ret

def bfs2(start):
    ret = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    target = grid[start[0]][start[1]]
    q.append(start)
    while(q):
        cur = q.popleft()
        ret.append(cur)
        cy = cur[0]
        cx = cur[1]
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if(0<= ny < len(grid) and 0<=nx<len(grid) and [ny,nx] not in q):
                if((target == 'R' or target == 'G') and (grid[ny][nx] == 'R' or grid[ny][nx] == 'G')):
                    if([ny,nx] not in ret):
                        q.append([ny,nx])
                elif(target == 'B' and grid[ny][nx] == 'B'):
                    if([ny,nx] not in ret):
                        q.append([ny,nx])
    return ret

visited = [[0 for i in range(len(grid))]for j in range(len(grid))]
default = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if(visited[i][j]==0):
            v = bfs([i,j])
            for k in v:
                visited[k[0]][k[1]] = 1
            default +=1 
ans = 0
visited = [[0 for i in range(len(grid))]for j in range(len(grid))]
for i in range(len(grid)):
    for j in range(len(grid)):
        if(visited[i][j]==0):
            v = bfs2([i,j])
            for k in v:
                visited[k[0]][k[1]] = 1
            ans +=1


print(default, ans)

