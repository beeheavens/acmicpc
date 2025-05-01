import sys
N, M, K = map(int,input().split()) #아이들, 친구 관계, 울음소리 조건
candy = list(map(int,input().split()))
node = [i for i in range(N)]

def find(target):
    if(node[target] != target):
        node[target] = find(node[target])
    return node[target]

def union(x,y):
    p_x = find(x)
    p_y = find(y)
    node[p_y] = p_x

for _ in range(M): #union-find로 집합을 형성
    a, b = map(int,sys.stdin.readline().split())
    union(a-1,b-1)

total_candy = {}
total_kid = {}

for idx,value in enumerate(node):
    target = find(value)
    if(target in total_candy):
        total_candy[target] += candy[idx]
        total_kid[target] += 1
    else:
        total_candy[target] = candy[idx]
        total_kid[target] = 1

temp = []

for i in total_candy:
    temp.append([total_kid[i],total_candy[i]])


dp = [-1 for i in range(K)]
dp[0] = 0
for i in temp:
    kid = i[0]
    c = i[1]
    for idx in range(K-1,-1,-1):
        target = idx - kid
        if(target >= 0):
            if(dp[target] != -1):
                if(dp[idx] == -1 or dp[idx] < dp[target] + c):
                    dp[idx] = dp[target] + c

print(max(dp))