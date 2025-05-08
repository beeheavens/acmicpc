import sys
sys.setrecursionlimit(10000000)
n = int(input())
data = list(map(int,input().split()))
dp = [[-1 for i in range(n)]for j in range(n)]

for i in range(n):
    dp[i][i] = 1 # 한칸짜리는 당연히 팰린드롬

def func(a,b):
    if(dp[a][b] != -1):
        return dp[a][b]
    else:
        if(a+1 == b):
            if(data[a] == data[b]):
                dp[a][b] = 1
                return 1
            else:
                dp[a][b] = 0
                return 0
        else:
            func(a+1,b-1)
            if(dp[a+1][b-1] == 0):
                dp[a][b] = 0
                return 0
            else:
                if(data[a] == data[b]):
                    dp[a][b] = 1
                    return 1
                else:
                    dp[a][b] = 0
                    return 0

t = int(input())
for _ in range(t):
    a, b = map(int,sys.stdin.readline().split())
    print(func(a-1,b-1))