import sys
import heapq
N, K = map(int, input().split())  # 구멍, 사용횟수
data = list(map(int, sys.stdin.readline().split()))

dict = {}
for idx, value in enumerate(data):
    if value not in dict:
        dict[value] = []
    dict[value].append(idx)  

ans = 0
using = []
cur = []
for i in data:
    temp = dict[i][0]
    del dict[i][0] # current를 제거
    if(len(using) < N): # 구멍이 남은 경우
        if(i in cur): #구멍이 남았는데 중복
            using.remove([-temp,i])
            if(len(dict[i])==0):
                heapq.heappush(using,[-K-10,i])
            else:
                heapq.heappush(using,[-dict[i][0],i])
            continue
        cur.append(i)
        if(len(dict[i]) == 0): #이제 다시 안쓰면
            heapq.heappush(using,[-K-10,i])
        else: #다시 쓰면
            heapq.heappush(using,[-dict[i][0],i])
    else: #구멍이 꽉 찬 경우
        if(i in cur):
            # 이미 구멍에 존재하는 경우 갱신을 시켜줘야 하는데
            using.remove([-temp,i])
            if(len(dict[i])==0):
                heapq.heappush(using,[-K-10,i])
            else:
                heapq.heappush(using,[-dict[i][0],i])
            continue
        ans += 1
        cur.remove(heapq.heappop(using)[1])
        cur.append(i)
        if(len(dict[i])==0):
            heapq.heappush(using,[-K-10,i])
        else:
            heapq.heappush(using,[-dict[i][0],i])
print(ans)
