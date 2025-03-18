from collections import deque

N, M = map(int,input().split())
paper = []
for i in range(N):
    paper.append(list(map(int,input().split())))

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def initialize():
    count = 0
    start = [0,0]
    deq = deque([start])
    while(deq):
        cur = deq.popleft()
        cy = cur[0]
        cx = cur[1]
        paper[cy][cx] = -1
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if(nx < 0 or ny < 0 or M <= nx or N <= ny):
                continue
            if(paper[ny][nx] == 0 and [ny,nx] not in deq):
                deq.append([ny,nx])
    for i in range(N):
        for j in range(M):
            if(paper[i][j] == 1):
                count+=1
    return count

def melt():
    melted = []
    for i in range(N):
        for j in range(M):
            if(paper[i][j] == 1):
                count = 0
                for d in range(4):
                    ny = i + dy[d]
                    nx = j + dx[d]
                    if(nx < 0 or ny < 0 or M <= nx or N <= ny):
                        continue
                    if(paper[ny][nx]==-1):
                        count += 1
                        if(count == 2):
                            break
                if(count >= 2):
                    melted.append([i,j])
                    paper[i][j] = 0
    return melted

def bfs(melted):
    for cheese in melted:
        if(paper[cheese[0]][cheese[1]] == -1):
            continue
        deq = deque([cheese])
        while(deq):
            cur = deq.popleft()
            cy = cur[0]
            cx = cur[1]
            paper[cy][cx] = -1
            for i in range(4):
                ny = cy + dy[i]
                nx = cx + dx[i]
                if(nx < 0 or ny < 0 or M <= nx or N <= ny):
                    continue
                if(paper[ny][nx] == 0 and [ny,nx] not in deq):
                    deq.append([ny,nx])
            
total_cheese = initialize()
ans = 0
while(total_cheese != 0):
    ans += 1
    melted_cheese = melt()
    total_cheese -= len(melted_cheese)
    bfs(melted_cheese)

print(ans)