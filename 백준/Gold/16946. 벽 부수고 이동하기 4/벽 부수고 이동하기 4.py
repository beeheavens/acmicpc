from collections import deque

N, M = map(int,input().split())
mm = [] #main map
for _ in range(N): # mm 에 맵 저장
    string = input()
    temp = []
    for i in string:
        temp.append(int(i))
    mm.append(temp)

def bfs(start,label):
    q = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q.append(start)
    ret = 0
    while(q):
        cy,cx = q.popleft()
        if(mm[cy][cx]!= 0):
            continue
        ret += 1
        mm[cy][cx] = label
        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]
            if(0<=ny<N and 0<=nx<M):
                if(mm[ny][nx] == 0):
                    q.append([ny,nx])
    return ret
                    
# 0이 이동가능한 곳, 이 부분을 덩어리 번호로 바꾼다.
label = 2 # 1은 벽이므로 2부터 시작하자
dict = {}
for i in range(N):
    for j in range(M):
        if(mm[i][j] == 0): # 0 이면
            total = bfs([i,j],label)
            dict[label] = total
            label += 1

dy = [0,0,-1,1]
dx = [1,-1,0,0]
for i in range(N):
    for j in range(M):
        if(mm[i][j] != 1):
            print(0,end="")
        else:
            ans = 0
            visited = []
            for d in range(4):
                ny = i + dy[d]
                nx = j + dx[d]
                if(0<=ny<N and 0<=nx<M):
                    if(mm[ny][nx] != 1 and mm[ny][nx] not in visited):
                        ans += dict[mm[ny][nx]]
                        visited.append(mm[ny][nx])
            print((ans+1)%10,end="")
    print()