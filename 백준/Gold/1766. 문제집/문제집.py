import heapq
from collections import deque

N, M = map(int,input().split())
prev = [[]for i in range(N)] # index = 먼저 풀어야 하는 문제
after = [[] for i in range(N)] # index = 이걸 풀면 뭘 풀 수 있어지는지

for _ in range(M):
    prev_problem, after_problem = map(int,input().split())
    prev[prev_problem-1].append(after_problem-1)
    after[after_problem-1].append(prev_problem-1)

hq = []
ans = []
for i in range(N):
    if(len(after[i])==0):
        heapq.heappush(hq,i)

while(hq):
    cur = heapq.heappop(hq)
    ans.append(cur)
    for i in prev[cur]:
        after[i].remove(cur)
        if(len(after[i])==0) : #더 이상 풀어야 할 문제가 없는 경우
            heapq.heappush(hq,i)

for i in range(N-1):
    print(ans[i]+1,end=" ")
print(ans[N-1]+1)