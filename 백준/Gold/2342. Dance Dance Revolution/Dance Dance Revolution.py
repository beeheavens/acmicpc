move = list(map(int,input().split()))

a = 0
b = 0

dp = [{} for i in range(len(move)+1)]
dp[0][(0,0)] = 0

def convert(prev, target):
    if(prev == 0):
        return 2
    elif(prev == 1):
        if(target == 1):
            return 1
        elif(target == 2 or target == 4):
            return 3
        elif(target == 3):
            return 4
    elif(prev == 2):
        if(target == 2):
            return 1
        elif(target == 1 or target == 3):
            return 3
        elif(target == 4):
            return 4
    elif(prev == 3):
        if(target == 3):
            return 1
        elif(target == 2 or target == 4):
            return 3
        elif(target == 1):
            return 4
    elif(prev == 4):
        if(target == 4):
            return 1
        elif(target == 1 or target == 3):
            return 3
        elif(target == 2):
            return 4

for i in range(len(move)):
    prev = dp[i]
    cur = dp[i+1]
    target = move[i]
    if(target == 0):
        break
    for j in prev:
        left = j[0]
        right = j[1]
        if(target != right):
            cur[(target,right)] = min(cur.get((target,right),float("inf")),(prev[j] + convert(left,target)))
        if(target != left):
            cur[(left,target)] = min(cur.get((left,target),float("inf")), prev[j] + convert(right,target))

ans = float("inf")
for i in dp[len(move)-1]:
    if(ans > dp[len(move)-1][i]):
        ans = dp[len(move)-1][i]

print(ans)
            
