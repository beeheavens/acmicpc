from collections import deque

N = int(input())
down = [[]for j in range(N)]
up = [[]for i in range(N)]
data = [[] for i in range(N)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    down[a-1].append([b-1,c]) #b-1까지 c만큼의 거리
    up[b-1].append([a-1,c])

check = [0 for i in range(N)]

deq = deque()
for i in range(N): # 리프 노드들을 넣어준다
    if(len(down[i])==0):
        deq.append(i)
        data[i].append(0)

visited = [0 for i in range(N)]

while(deq):
    cur = deq.popleft()
    if(visited[cur] == 1):
        continue
    visited[cur] = 1
    if(cur != 0):
        check[up[cur][0][0]] += 1
        if(check[up[cur][0][0]] == len(down[up[cur][0][0]])):
            deq.append(up[cur][0][0])#부모 노드 추가
    for i in down[cur]:
        data[cur].append(max(data[i[0]]) + i[1])

ans = []

for i in data:
    if(len(i) >= 2):
        i.sort(reverse=True)
        ans.append(i[0]+i[1])
    elif(len(i)==1):
        ans.append(i[0])
    else:
        ans.append(0)

print(max(ans))