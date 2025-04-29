str1 = input()
str2 = input()
dp = [['' for i in range(len(str1)+1)]for j in range(len(str2)+1)]

for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        if(str1[j-1]==str2[i-1]):
            dp[i][j] = dp[i-1][j-1] + str1[j-1]
        else:
            if(len(dp[i-1][j]) > len(dp[i][j-1])):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[len(str2)][len(str1)]),dp[len(str2)][len(str1)])