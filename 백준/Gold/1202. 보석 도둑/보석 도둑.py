import sys
import heapq

N, K = map(int,input().split())

jewel = []
bag = []
for _ in range(N):
    jewel.append(list(map(int,sys.stdin.readline().split()))) # 무게, 가치

for _ in range(K):
    bag.append(int(sys.stdin.readline()))

jewel.sort(key = lambda x : (-x[0]))
bag.sort(reverse=True)


heap = []
ans = 0
while(bag):
    cur_bag = bag.pop() # 가장 작은 가방
    while(jewel):
        w, v = jewel.pop()
        if(w <= cur_bag):
            heapq.heappush(heap,-v)
        else:
            jewel.append([w,v])
            break
    if(heap):
        ans += heapq.heappop(heap) * -1

print(ans)