n, k = map(int,input().split())
coins = []
dp = [0] * (k+1)
for _ in range(n):
    coins.append(int(input()))

dp[0] = 1
for coin in coins:
    for i in range(k+1):
        target = i + coin
        if(target <=k):
            dp[target] += dp[i]

print(dp[k])