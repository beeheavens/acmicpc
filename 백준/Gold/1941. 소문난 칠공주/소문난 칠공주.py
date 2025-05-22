from itertools import combinations
from collections import deque


classroom = []
for _ in range(5):
    classroom.append(input())

position = []
for i in range(5):
    for j in range(5):
        position.append([i,j])

combi = list(combinations(position,7))
ans = 0

for i in combi:
    temp_map = [[0 for i in range(5)]for j in range(5)]
    for pos in i:
        y,x = pos
        temp_map[y][x] = 1
    q = deque()
    q.append(i[0])
    connected = 0
    visited = []
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    while(q):
        cur = q.popleft()
        if(cur in visited):
            continue
        visited.append(cur)
        cy = cur[0]
        cx = cur[1]
        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]
            if(0<=ny<5 and 0<=nx<5):
                if(temp_map[ny][nx] == 1 and [ny,nx] not in visited):
                    q.append([ny,nx])
    if(len(visited)==7): #다 연결되는 경우
        y = 0
        s = 0
        for i in visited:
            y,x = i 
            if(classroom[y][x] == 'Y'):
                y += 1
            else:
                s += 1
        if(s >= 4):
            ans += 1

print(ans)