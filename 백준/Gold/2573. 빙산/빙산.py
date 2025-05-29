from collections import deque

n, m = map(int,input().split())
mapp = []
for _ in range(n):
    mapp.append(list(map(int,input().split())))

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def melt():
    # 녹는 양을 저장할 배열
    melt_amount = [[0] * m for _ in range(n)]
    
    # 각 빙산의 녹는 양을 한 번에 계산
    for i in range(n):
        for j in range(m):
            if mapp[i][j] > 0:
                for d in range(4):
                    ny, nx = i + dy[d], j + dx[d]
                    if 0 <= ny < n and 0 <= nx < m and mapp[ny][nx] == 0:
                        melt_amount[i][j] += 1
    
    # 한 번에 녹이기
    for i in range(n):
        for j in range(m):
            if mapp[i][j] > 0:
                mapp[i][j] = max(0, mapp[i][j] - melt_amount[i][j])

def bfs():
    visited = [[False] * m for _ in range(n)]
    num = 0
    
    for i in range(n):
        for j in range(m):
            if mapp[i][j] > 0 and not visited[i][j]:
                num += 1
                q = deque([(i, j)])
                visited[i][j] = True
                
                while q:
                    cy, cx = q.popleft()
                    for d in range(4):
                        ny, nx = cy + dy[d], cx + dx[d]
                        if (0 <= ny < n and 0 <= nx < m and 
                            mapp[ny][nx] > 0 and not visited[ny][nx]):
                            visited[ny][nx] = True
                            q.append((ny, nx))
    return num

ans = 0
while True:
    melt()
    ans += 1
    group = bfs()
    
    if group == 0:
        print(0)
        break
    elif group >= 2:
        print(ans)
        break