import heapq
import sys
N, M, X = map(int, sys.stdin.readline().split())

# 인접 리스트로 변경
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))  # (도착노드, 비용)
            
def dijkstra(start, end):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    queue = [(0, start)]
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
                
    return distance[end]

go = []
for i in range(1, N+1):
    go.append(dijkstra(i, X))
    
back = []
for i in range(1, N+1):
    back.append(dijkstra(X, i))

ans = []
for i in range(N):
    ans.append(go[i] + back[i])

print(max(ans))