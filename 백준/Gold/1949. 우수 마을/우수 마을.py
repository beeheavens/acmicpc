from collections import deque
n = int(input())
people = list(map(int,input().split()))
tree = [[]for i in range(n)]
leaf_checker = [[]for i in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    leaf_checker[a-1].append(b-1)
    leaf_checker[b-1].append(a-1)
dp = [[] for i in range(n)]

q = deque()

for i in range(n):
    if(len(tree[i])==1): #leaf node
        q.append(i)

while(q):
    cur = q.popleft()
    #해당 값의 0과 1을 각각 계산
    #0부터 계산해보자. 일반 마을일 경우
    temp = 0
    for connected in tree[cur]: #연결된 노드
        if(len(dp[connected]) != 0): #방문해서 값이 있는 노드면
            temp += max(dp[connected][1],dp[connected][0]) #우수 마을일 때의 값을 빨아들임
    dp[cur].append(temp)
    #1. 우수 마을이 되었을 경우
    temp = 0
    for connected in tree[cur]:
        if(len(dp[connected])!=0):
            temp += dp[connected][0]
    dp[cur].append(temp+people[cur])
    #이제 방문한 노드들 연결을 끊어줘야겠지
    for connected in tree[cur]:
        leaf_checker[connected].remove(cur) # 현재 노드를 없애줘요
        if(len(leaf_checker[connected])==1): #이제 부모만 남은 경우
            q.append(connected)
            
print(max(max(dp)))