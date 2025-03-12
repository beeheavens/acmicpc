import sys
N, M = input().split()
N = int(N)
M = int(M)
vertices = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    a,b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    vertices[a-1][b-1] = 1
    vertices[b-1][a-1] = 1

not_visited = [i for i in range(N)]

ans = 0
while(len(not_visited) > 0):
    ans += 1
    cur = not_visited[0]
    bfs = [cur]
    while(len(bfs)>0):
        now = bfs[0]
        del bfs[0]
        not_visited.remove(now)
        for idx,value in enumerate(vertices[now]):
            if(value == 1 and idx in not_visited and idx not in bfs):
                bfs.append(idx)

print(ans)