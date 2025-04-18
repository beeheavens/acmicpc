from collections import deque

N, M = map(int,input().split())
data = [[]for j in range(N)]
back = [[]for j in range(N)]

for _ in range(M):
    A, B = map(int,input().split())
    data[B-1].append(A-1)
    back[A-1].append(B-1)

#맨 앞에 설 사람들 선택
dq = deque()
for i in range(N):
    if(len(data[i])==0):
        dq.append(i)

ans = []
while(dq):
    cur = dq.popleft()
    ans.append(cur+1)
    for i in back[cur]:
        data[i].remove(cur)
        if(len(data[i])==0):
            dq.append(i)


for i in range(len(ans)-1):
    print(ans[i],end=" ")
print(ans[len(ans)-1])