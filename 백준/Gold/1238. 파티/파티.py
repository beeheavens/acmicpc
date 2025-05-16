import heapq
import sys
N, M, X = map(int, sys.stdin.readline().split())

# 정방향과 역방향 그래프 생성
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))  # 정방향 그래프
    reverse_graph[b].append((a, c))  # 역방향 그래프
            
def dijkstra(start, g):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    queue = [(0, start)]
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for next_node, cost in g[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
                
    return distance

# X에서 모든 노드로 가는 최단 거리 (정방향)
go = dijkstra(X, graph)

# 모든 노드에서 X로 가는 최단 거리 (역방향)
back = dijkstra(X, reverse_graph)

ans = 0
for i in range(1, N+1):
    if i != X:
        ans = max(ans, go[i] + back[i])

print(ans)