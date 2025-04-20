from collections import deque
N = int(input())
nodes = list(map(int,input().split()))
target = int(input())
child = [[] for i in range(N)]
root = 0
for i in range(N):
    parents = nodes[i]
    if(parents == -1):
        root = i
        continue
    if(i == target):
        continue
    else:
        child[parents].append(i)
ans = 0
bfs = deque()
bfs.append(root)
while(bfs):
    cur = bfs.popleft()
    if(cur==target):
        continue
    if(len(child[cur])==0): # leaf node
        ans += 1
    else:
        for i in child[cur]:
            bfs.append(i)
print(ans)