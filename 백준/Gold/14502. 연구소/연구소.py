from itertools import combinations
from collections import deque

N, M = map(int,input().split())
mapp = []
for _ in range(N):
    mapp.append(list(map(int,input().split())))

virus = []
empty = []
for i in range(N):
    for j in range(M):
        if mapp[i][j] == 0:
            empty.append([i,j])
        elif mapp[i][j] == 2:
            virus.append([i,j])

walls = list(combinations(empty,3))


dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(source,mapp):
    temp = [row[:] for row in mapp]
    q = deque()
    q.append(source)
    while(q):
        cy,cx = q.popleft()
        if(temp[cy][cx] == 2 and [cy,cx] != source):
            continue
        temp[cy][cx] = 2
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if(0<=ny<N and 0<=nx<M):
                if(temp[ny][nx] == 0):
                    q.append([ny,nx])
    return temp

def count(mapp):
    ret = 0
    for i in range(N):
        for j in range(M):
            if(mapp[i][j]==0):
                ret += 1
    return ret

max = 0
for wall in walls:
    temp_map = [row[:]for row in mapp]
    for w in wall:
        temp_map[w[0]][w[1]] = 1
    for v in virus:
        temp_map = bfs(v,temp_map)
    c = count(temp_map)
    if(max<c):
        max = c

print(max)