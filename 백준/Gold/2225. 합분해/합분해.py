N, K = map(int,input().split())

dp = [[0 for i in range(N+1)] for j in range(K)]
for i in range(N+1):
    dp[0][i] = 1 # 일단 수 하나만

for i in range(K-1):
    for k in range(N+1):
        for j in range(N+1):
            cur = dp[i][j]
            target_y = i + 1
            target_x = j + k
            if(target_y <= K-1 and target_x <= N):
                dp[target_y][target_x] += cur


sum = dp[K-1][N]

print(sum % 1000000000)