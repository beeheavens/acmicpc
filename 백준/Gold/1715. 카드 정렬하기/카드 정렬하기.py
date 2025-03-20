import heapq

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

ans = 0
if(len(num) == 0 ): #값이 하나일 때
    ans = num[0]
else: #아니면
    heapq.heapify(num) #heapq 생성
    while(len(num)>1):
        A = heapq.heappop(num)
        B = heapq.heappop(num)
        ans += A + B
        heapq.heappush(num,A+B)

print(ans)
    