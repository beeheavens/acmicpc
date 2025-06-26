N = int(input())
data = list(map(int,input().split()))
stack = []
ans = []
for i in range(N):
    cur = data[i]
    flag = 0 
    while stack:
        target_idx = stack[len(stack)-1]
        if cur < data[target_idx]:
            ans.append(target_idx+1)
            stack.append(i)
            flag = 1
            break
        elif cur > data[target_idx]:
            del stack[len(stack)-1]
    
    if flag == 0:
        ans.append(0)
        stack.append(i)

for i in ans:
    print(i,end=" ")