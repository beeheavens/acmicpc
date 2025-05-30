N, M = map(int,input().split())
cost = []
judge = []
for _ in range(N):
    cost.append(int(input()))

for _ in range(M):
    judge.append(int(input()))

vote = [0 for i in range(N)]
for j in judge:
    for i in range(N):
        if(cost[i] <= j):
            vote[i] += 1
            break

max = 0
ans = 0
for i in range(len(vote)):
    if(max < vote[i]):
        max = vote[i]
        ans = i
print(ans+1)