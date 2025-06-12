from collections import deque

R, C = map(int,input().split())
chess = []
for _ in range(R):
    chess.append(list(map(int,input().split())))

dest = [[0 for i in range(C)]for j in range(R)]
dy = [0,1,1,1,0,-1,-1,-1]
dx = [1,1,0,-1,-1,-1,0,1]


def search(source):
    q = deque()
    q.append(source)
    route = []
    while q:
        cur = q.popleft()
        route.append(cur)
        cy, cx = cur
        if(dest[cy][cx] != 0):
            route.append(dest[cy][cx])
            break
        min = chess[cy][cx]
        ty = 0 
        tx = 0
        for i in range(8):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if(0<=ny<R and 0<=nx<C):
                if chess[ny][nx] < min:
                    min = chess[ny][nx]
                    ty = ny
                    tx = nx
        if min != chess[cy][cx]:
            q.append([ty,tx])
    d = route[len(route)-1] #최종지
    for i in route:
        cy, cx = i
        dest[cy][cx] = d

for i in range(R):
    for j in range(C):
        if(dest[i][j] == 0): #아직 최종지가 결정되지 않은 칸이면,
            search([i,j])

ans = [[0 for i in range(C)]for j in range(R)]

for i in range(R):
    for j in range(C):
        dy,dx = dest[i][j]
        ans[dy][dx] += 1

for i in range(R):
    for j in range(C):
        print(ans[i][j],end=" ")
    print()
