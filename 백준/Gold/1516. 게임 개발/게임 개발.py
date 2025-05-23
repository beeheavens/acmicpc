from collections import deque

N = int(input())
f_graph = [[] for i in range(N)] # 선행 해야 될 것들
b_graph = [[] for i in range(N)] # 완료되면 가능해지는 것들
b_graph_copied = [[] for i in range(N)]
time = []
min_time = [0 for i in range(N)]

for t in range(N):
    data= list(map(int,input().split()))
    time.append(data[0])
    del data[0]
    for i in range(len(data)-1):
        temp = data[i] -1
        f_graph[temp].append(t)
        b_graph[t].append(temp)
        b_graph_copied[t].append(temp)


q = deque()

for i in range(N):
    if(len(b_graph[i])==0):
        q.append(i)

while(q):
    cur = q.popleft()
    #시간 결정
    if(len(b_graph_copied[cur])==0):
        min_time[cur] = time[cur]
    else:
        temp = []
        for i in b_graph_copied[cur]:
            temp.append(min_time[i])
        min_time[cur] = max(temp) + time[cur]
    
    for child in f_graph[cur]:
        b_graph[child].remove(cur)
        if(len(b_graph[child])==0):
            q.append(child)

for i in min_time:
    print(i)