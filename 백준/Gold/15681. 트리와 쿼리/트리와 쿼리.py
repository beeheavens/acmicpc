from collections import deque
import sys

sys.setrecursionlimit(100000)
N, R, Q = map(int,input().split())
tree = [[]for j in range(N)]
level = [-1 for i in range(N)]
queries = []
for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

for _ in range(Q):
    queries.append(int(input()))

dq = deque()
dq.append(R-1)
level[R-1] = 0
dir_tree = [[]for i in range(N)]
#레벨 만듬
while(dq):
    cur = dq.popleft()
    for i in tree[cur]:
        if(level[i]==-1):
            level[i] = level[cur] + 1
            dir_tree[cur].append(i)
            dq.append(i)

subtree_num = [0 for i in range(N)]

def subtree(node):
    ans = 1
    for i in dir_tree[node]:
        ans += subtree(i)
    subtree_num[node] = ans
    return ans

subtree(R-1)
for i in queries:
    print(subtree_num[i-1])


