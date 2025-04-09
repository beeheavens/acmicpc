# Version 1 O(N * K)
N, K = map(int,input().split())
items = []
dp = [-1] * (K+1)
for _ in range(N):
    items.append(list(map(int,input().split())))

dp[0] = 0

for item in items:
    w, v = item
    for idx in range(K,-1,-1): # 거꾸로
        target = idx - w
        if(target >= 0): # 인덱스 체크
            if(dp[target] != -1):
                temp = dp[target] + v
                if(dp[idx] < temp):
                    dp[idx] = temp

print(max(dp))