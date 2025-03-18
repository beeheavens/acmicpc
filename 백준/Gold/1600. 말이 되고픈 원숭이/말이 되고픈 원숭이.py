import sys
from collections import deque

K = int(input())
W, H = input().split()
W = int(W)
H = int(H)

board = []
for _ in range(H):
    board.append(list(map(int,sys.stdin.readline().split())))

horse_y = [1,2,2,1,-1,-2,-2,-1] # 말 움직임
horse_x = [2,1,-1,-2,-2,-1,1,2]
dy = [0,1,0,-1]
dx = [1,0,-1,0]

dp = [[[-1 for i in range(K+1)]for j in range(W)]for k in range(H)]
deq = deque([[0,0,0]])
dp[0][0][0] = 0
flag = 0
while(deq):
    target = deq.popleft()
    cur_y = target[0]
    cur_x = target[1]
    horse_move = target[2]
    if(cur_y == H-1 and cur_x == W-1):
        print(dp[cur_y][cur_x][horse_move])
        flag = 1
        break
    if(horse_move < K):
        for i in range(8):
            next_y = cur_y + horse_y[i]
            next_x = cur_x + horse_x[i]
            next_horse = horse_move +1
            if(0<=next_y < H and 0<=next_x < W):
                if(dp[next_y][next_x][next_horse]==-1 and board[next_y][next_x] == 0):
                    dp[next_y][next_x][next_horse] = dp[cur_y][cur_x][horse_move] + 1
                    deq.append([next_y,next_x,next_horse])
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if(0<=next_y < H and 0<=next_x < W):
            if(dp[next_y][next_x][horse_move]==-1 and board[next_y][next_x]==0):
                dp[next_y][next_x][horse_move] = dp[cur_y][cur_x][horse_move] + 1
                deq.append([next_y,next_x,horse_move])

if(flag==0):
    print(-1)
