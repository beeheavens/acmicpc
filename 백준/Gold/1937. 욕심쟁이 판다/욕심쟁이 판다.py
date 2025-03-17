import sys
sys.setrecursionlimit(100000000)
N = int(input())
forest = []
dp = [[0 for i in range(N)] for j in range(N)]
for _ in range(N):#input
    forest.append(list(map(int,sys.stdin.readline().split())))


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(start):
    cur_y = start[0]
    cur_x = start[1]
    next_targets = []
    for i in range(4):
        next_y = cur_y + dy[i]
        next_x = cur_x + dx[i]
        if(0 <= next_y < N and 0 <= next_x < N): #index 확인
            if(forest[next_y][next_x] > forest[cur_y][cur_x]):
                if(dp[next_y][next_x] == 0):
                    next_targets.append(dfs([next_y,next_x]))
                else:
                    next_targets.append(dp[next_y][next_x])
    if(len(next_targets) == 0):
        dp[cur_y][cur_x] = 1
        return 1
    else:
        num = max(next_targets) + 1
        if(num > dp[cur_y][cur_x]):
            dp[cur_y][cur_x] = num
        return dp[cur_y][cur_x]
            

ans = 0
for i in range(N):
    for j in range(N):
        if(dp[i][j] == 0):
            ans = max(ans,dfs([i,j]))
    
print(ans)
