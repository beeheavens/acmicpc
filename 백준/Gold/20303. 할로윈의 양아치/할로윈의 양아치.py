import sys
from collections import deque
N, M, K = map(int,input().split()) #아이들, 친구 관계, 울음소리 조건
candy = list(map(int,input().split()))
node = [i for i in range(N)]

visited = [0 for i in range(N)]
graph = [[]for i in range(N)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(start):
    deq = deque()
    deq.append(start)
    kids = 0
    candies = 0
    while(deq):
        cur = deq.popleft()
        if(visited[cur]==1):
            continue
        kids += 1
        candies += candy[cur]
        visited[cur] = 1
        for node in graph[cur]:
            if(visited[node] == 0): #아직 방문 안한 경우
                deq.append(node)
    return kids,candies

temp = []
for i in range(N):
    if(visited[i] == 0):
        k,c = bfs(i)
        temp.append([k,c])

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