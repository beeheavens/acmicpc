import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
singer = [[]for i in range(n)]
after = [[]for i in range(n)]

for _ in range(m):
    data = list(map(int,input().split()))
    del data[0]
    for i in range(len(data)-1,-1,-1):
        for j in range(i):
            target = data[i] - 1
            front = data[j] - 1
            if(front not in singer[target]):
                singer[target].append(front)
            if(target not in after[front]):
                after[front].append(target)

ans = []
q = deque()
for i in range(n):
    if(len(singer[i])==0):
        q.append(i)

while(q):
    cur = q.popleft()
    if(cur in ans):
        continue
    ans.append(cur)
    for next in after[cur]:
        singer[next].remove(cur)
        if(len(singer[next])==0):
            q.append(next)

if(len(ans) != n):
    print(0)
else:
    for i in ans:
        print(i+1,end=" ")